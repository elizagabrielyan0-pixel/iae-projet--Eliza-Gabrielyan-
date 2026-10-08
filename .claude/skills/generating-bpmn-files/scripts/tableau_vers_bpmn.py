#!/usr/bin/env python3
"""Traduit le tableau du processus d'un livrable preparation-bpmn-as-is en fichier .bpmn pour Camunda Modeler.

Usage :
    python3 tableau_vers_bpmn.py <livrable.md> <sortie.bpmn>
    python3 tableau_vers_bpmn.py --verifier <fichier.bpmn>

Le script recopie le tableau principal (section « 1. Tableau du processus », sans les tableaux
« Détail de SPx ») : une ligne = un élément, rien d'ajouté sauf les annotations de statut.
Il calcule la mise en page (gauche à droite, couloirs, aucun chevauchement, flux sans traverser
de forme), puis vérifie le fichier produit. Python 3 standard, aucune installation.
Code de sortie : 0 = fichier propre ; 1 = fichier produit avec anomalies listées ; 2 = erreur.
"""
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

# ---------------------------------------------------------------- lecture du livrable

TYPES = {
    "tâche utilisateur": ("userTask", None), "tâche manuelle": ("manualTask", None),
    "tâche envoi": ("sendTask", None), "tâche service": ("serviceTask", None),
    "sous-processus": ("subProcess", None),
    "début": ("startEvent", None), "début message": ("startEvent", "message"),
    "début minuterie": ("startEvent", "timer"),
    "fin": ("endEvent", None), "fin message": ("endEvent", "message"),
    "minuterie intermédiaire": ("intermediateCatchEvent", "timer"),
    "message reçu": ("intermediateCatchEvent", "message"),
    "message envoyé": ("intermediateThrowEvent", "message"),
    "lien envoi": ("intermediateThrowEvent", "link"),
    "lien réception": ("intermediateCatchEvent", "link"),
    "passerelle exclusive": ("exclusiveGateway", None), "passerelle parallèle": ("parallelGateway", None),
    "passerelle inclusive": ("inclusiveGateway", None),
    "passerelle basée sur les événements": ("eventBasedGateway", None),
    "participant externe": ("participant", None),
}
MSG_RE = re.compile(r"Message\s*«\s*(.+?)\s*»\s*→\s*([A-Za-z][\w-]*)")
NONE = {"", "—", "-", "–"}


def sans_accent(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def ident(s):
    return re.sub(r"[^A-Za-z0-9_]", "_", sans_accent(s)).strip("_") or "X"


def lire_livrable(chemin):
    texte = open(chemin, encoding="utf-8").read()
    principal = re.split(r"\n#{2,3}\s*(?:Détail|2\.)", texte)[0]
    lignes = []
    for brut in principal.splitlines():
        if not brut.startswith("|"):
            continue
        cells = [c.strip() for c in brut.strip().strip("|").split("|")]
        if len(cells) < 8 or cells[0] in ("ID", "") or set(cells[0]) <= set("-: "):
            continue
        lignes.append(dict(zip(["id", "pc", "label", "type", "cond", "next", "source", "statut"], cells[:8])))
    # Pour chaque ID : la première question « Bloquant pour la modélisation » qui le cite,
    # sinon la première question qui le cite.
    questions, bloquantes = {}, {}
    for q in re.finditer(r"^\s*-?\s*(Q\d+)\s*—\s*((?:\[[^\]]+\]\s*)+)—?\s*(.*)$", texte, re.M):
        bloquante = q.group(3).lower().startswith("bloquant")
        for rid in re.findall(r"\[([^\]]+)\]", q.group(2)):
            questions.setdefault(rid.strip(), q.group(1))
            if bloquante:
                bloquantes.setdefault(rid.strip(), q.group(1))
    questions.update(bloquantes)
    return lignes, questions


# ---------------------------------------------------------------- modèle

class Modele:
    def __init__(self, lignes, questions):
        self.anomalies = []
        self.externes, self.noeuds, self.ordre, self.couloirs = {}, {}, [], []
        self.seq, self.msg = [], []
        self.interne = None
        for l in lignes:
            t = l["type"].strip().lower()
            if t not in TYPES:
                self.anomalies.append(f"[{l['id']}] type BPMN inconnu « {l['type']} » : élément non créé")
                continue
            if TYPES[t][0] == "participant":
                self.externes[l["id"]] = {"name": l["label"] if l["label"] not in NONE else l["pc"], "row": l}
                continue
            if " / " in l["pc"]:
                part, lane = l["pc"].split(" / ", 1)
            else:
                part, lane = (self.interne or "Processus"), l["pc"]
                self.anomalies.append(f"[{l['id']}] colonne Participant / Couloir sans « / » : couloir « {lane} » utilisé")
            self.interne = self.interne or part.strip()
            lane = lane.strip()
            if lane not in self.couloirs:
                self.couloirs.append(lane)
            tag, ev = TYPES[t]
            self.noeuds[l["id"]] = {"id": l["id"], "xid": "E_" + ident(l["id"]), "tag": tag, "ev": ev,
                                    "label": "" if l["label"] in NONE else l["label"], "lane": lane,
                                    "statut": l["statut"], "row": l, "inc": [], "out": []}
            self.ordre.append(l["id"])
        self.questions = questions
        tous = set(self.noeuds) | set(self.externes)
        for l in lignes:
            src = l["id"]
            if src not in tous:
                continue
            conds = {}
            if l["cond"] not in NONE:
                for part in re.split(r"\s;\s|;\s", l["cond"]):
                    if ":" in part:
                        k, v = part.split(":", 1)
                        conds[k.strip()] = v.strip()
            reste = MSG_RE.sub("", l["next"])
            for nom, cible in MSG_RE.findall(l["next"]):
                if cible not in tous:
                    self.anomalies.append(f"[{src}] message « {nom} » vers [{cible}] qui n'existe pas : flux non créé")
                elif (src in self.externes) == (cible in self.externes):
                    self.anomalies.append(f"[{src}] message « {nom} » vers [{cible}] dans le même participant : flux non créé")
                else:
                    self.msg.append((src, cible, nom))
            if src in self.externes:
                continue
            for cible in [c.strip() for c in reste.split(";")]:
                if cible in NONE:
                    continue
                if cible in self.externes:
                    self.anomalies.append(f"[{src}] lien vers le participant externe [{cible}] sans « Message « … » → » : flux non créé")
                elif cible not in self.noeuds:
                    self.anomalies.append(f"[{src}] élément suivant [{cible}] introuvable : flux non créé")
                else:
                    self.seq.append((src, cible, conds.get(cible, "")))
        for s, c, _ in self.seq:
            self.noeuds[s]["out"].append((s, c))
            self.noeuds[c]["inc"].append((s, c))
        for nid, n in self.noeuds.items():
            if n["tag"] in ("exclusiveGateway", "inclusiveGateway") and len(n["out"]) > 1:
                for s, c, cond in self.seq:
                    if s == nid and not cond:
                        self.anomalies.append(f"[{nid}] branche vers [{c}] sans condition")
            if n["tag"] == "endEvent" and n["out"]:
                self.anomalies.append(f"[{nid}] une fin a un élément suivant")
            if n["tag"] not in ("startEvent", "intermediateCatchEvent") and not n["inc"] and not (n["ev"] == "link"):
                if not any(c == nid for _, c, _ in self.msg):
                    self.anomalies.append(f"[{nid}] aucun élément ne mène à cet élément")

    def annotation(self, n):
        q = self.questions.get(n["id"])
        st = n["statut"].lower()
        if st.startswith("supposé"):
            return "Supposé — à confirmer"
        if st.startswith("non confirmé"):
            return f"Non confirmé — voir question {q}" if q else "Non confirmé — voir points signalés"
        if st.startswith("à préciser") and not n["label"].lower().startswith("à préciser"):
            return f"À préciser — voir question {q}" if q else "À préciser — voir points signalés"
        return None


# ---------------------------------------------------------------- mise en page

SIZE = {"task": (100, 80), "subProcess": (100, 80), "event": (36, 36), "gateway": (50, 50)}
COL, X0, POOL_HEAD, EXT_H, EXT_GAP = 180, 150, 30, 100, 50
OFFSETS = (0, -8, 8, -16, 16, -24, 24)


def centre_col(c):
    return X0 + POOL_HEAD + 40 + COL / 2 + c * COL


def taille(tag):
    if tag.endswith("Task") or tag == "subProcess":
        return SIZE["task"]
    if tag.endswith("Gateway"):
        return SIZE["gateway"]
    return SIZE["event"]


def rangs(m):
    succ = {k: [] for k in m.noeuds}
    for s, c, _ in m.seq:
        succ[s].append(c)
    retour, etat = set(), {}

    def dfs(u):
        etat[u] = 1
        for v in succ[u]:
            if etat.get(v) == 1:
                retour.add((u, v))
            elif v not in etat:
                dfs(v)
        etat[u] = 2
    sys.setrecursionlimit(10000)
    departs = [k for k in m.ordre if not m.noeuds[k]["inc"]]
    for k in departs + m.ordre:
        if k not in etat:
            dfs(k)
    rang = {k: 0 for k in m.noeuds}
    for _ in range(len(m.noeuds) + 1):
        change = False
        for s, c, _ in m.seq:
            if (s, c) not in retour and rang[c] < rang[s] + 1:
                rang[c] = rang[s] + 1
                change = True
        if not change:
            break
    for k, n in m.noeuds.items():  # lien réception : juste avant son suivant
        if n["ev"] == "link" and n["tag"] == "intermediateCatchEvent" and succ[k]:
            rang[k] = max(0, min(rang[c] for c in succ[k]) - 1)
    return rang


class Plan:
    def __init__(self, m):
        self.m = m
        rang = rangs(m)
        self.ncols = max(rang.values(), default=0) + 1
        # pile des éléments par (couloir, colonne)
        pile = {}
        for k in m.ordre:
            n = m.noeuds[k]
            pile.setdefault((n["lane"], rang[k]), []).append(k)
        annot_lane = {ln: any(m.annotation(m.noeuds[k]) for k in m.ordre if m.noeuds[k]["lane"] == ln) for ln in m.couloirs}
        self.slot_h = {ln: 190 if annot_lane[ln] else 150 for ln in m.couloirs}
        nslots = {ln: max([len(v) for (l2, _), v in pile.items() if l2 == ln] or [1]) for ln in m.couloirs}
        # participants externes : alternance au-dessus / au-dessous du participant interne
        ext = list(m.externes)
        dessus, dessous = ext[0::2], ext[1::2]
        self.pool_w = POOL_HEAD + 40 + self.ncols * COL + 20
        y = 60
        self.ext = {}
        for i, e in enumerate(dessus[::-1]):
            self.ext[e] = (X0, y, self.pool_w, EXT_H, "dessus")
            y += EXT_H + EXT_GAP
        self.pool_y = y
        self.lane = {}
        for ln in m.couloirs:
            h = nslots[ln] * self.slot_h[ln]
            self.lane[ln] = (X0 + POOL_HEAD, y, self.pool_w - POOL_HEAD, h)
            y += h
        self.pool_h = y - self.pool_y
        y += EXT_GAP
        for e in dessous:
            self.ext[e] = (X0, y, self.pool_w, EXT_H, "dessous")
            y += EXT_H + EXT_GAP
        # formes
        self.shape, self.slot, self.col = {}, {}, {}
        for (ln, c), ids in pile.items():
            lx, ly, _, _ = self.lane[ln]
            for i, k in enumerate(ids):
                w, h = taille(m.noeuds[k]["tag"])
                cx = centre_col(c)
                st = ly + i * self.slot_h[ln]
                cy = st + (70 if self.slot_h[ln] == 190 else 75)
                self.shape[k] = (cx - w / 2, cy - h / 2, w, h)
                self.slot[k] = (st, st + self.slot_h[ln])
                self.col[k] = c
        self.annot = {}
        for k in m.ordre:
            txt = m.annotation(m.noeuds[k])
            if txt:
                x, y0, w, h = self.shape[k]
                cx = x + w / 2
                self.annot[k] = (txt, (cx - 60, self.slot[k][0] + 125, 120, 45))
        self.traces = []
        self.labels = {}
        self.edges = {}
        self.problemes = []
        self.route_tout()

    # -- outils géométriques
    def obstacles(self, exclure):
        out = []
        for k, b in self.shape.items():
            if k not in exclure:
                out.append(b)
        for k, (_, b) in self.annot.items():
            out.append(b)
        return out

    @staticmethod
    def coupe(p, q, b):
        x, y, w, h = b
        x1, x2 = sorted((p[0], q[0]))
        y1, y2 = sorted((p[1], q[1]))
        return x1 < x + w - 1 and x2 > x + 1 and y1 < y + h - 1 and y2 > y + 1

    def libre(self, pts, exclure):
        obs = self.obstacles(exclure)
        if any(self.coupe(pts[i - 1], pts[i], b) for i in range(1, len(pts)) for b in obs):
            return False
        for i in range(1, len(pts)):  # jamais posé sur un trait déjà tracé
            p1, p2 = pts[i - 1], pts[i]
            for q1, q2, bouts in self.traces:
                if bouts & exclure:
                    continue
                for k in (0, 1):
                    if p1[k] == p2[k] == q1[k] == q2[k]:
                        lo = max(min(p1[1 - k], p2[1 - k]), min(q1[1 - k], q2[1 - k]))
                        hi = min(max(p1[1 - k], p2[1 - k]), max(q1[1 - k], q2[1 - k]))
                        if hi - lo > 2:
                            return False
        return True

    def trace(self, pts, bouts):
        for i in range(1, len(pts)):
            self.traces.append((pts[i - 1], pts[i], set(bouts)))

    @staticmethod
    def gaps(col, cote=+1):
        base = centre_col(col) + cote * COL / 2
        return [base + o for o in OFFSETS]

    # -- flux de séquence
    def route_seq(self, s, t):
        sx, sy, sw, sh = self.shape[s]
        tx, ty, tw, th = self.shape[t]
        scx, scy, tcx, tcy = sx + sw / 2, sy + sh / 2, tx + tw / 2, ty + th / 2
        ex = {s, t}
        cands = []
        if self.col[t] > self.col[s]:
            if scy == tcy:
                cands.append([(sx + sw, scy), (tx, tcy)])
            for g in self.gaps(self.col[s]) + self.gaps(self.col[t], -1):
                cands.append([(sx + sw, scy), (g, scy), (g, tcy), (tx, tcy)])
            for cy in (self.slot[s][1] - 8, self.slot[s][0] + 8):
                bord = (scx, sy + sh) if cy > scy else (scx, sy)
                for g in self.gaps(self.col[t], -1):
                    cands.append([bord, (scx, cy), (g, cy), (g, tcy), (tx, tcy)])
        else:  # retour en arrière ou même colonne : passage par le couloir de circulation
            for cy in (self.slot[s][1] - 8, self.slot[s][0] + 8):
                bs = (scx, sy + sh) if cy > scy else (scx, sy)
                if self.slot[t] == self.slot[s]:
                    bt = (tcx, ty + th) if cy > tcy else (tcx, ty)
                    cands.append([bs, (scx, cy), (tcx, cy), bt])
                for g in self.gaps(self.col[t], -1):
                    cands.append([bs, (scx, cy), (g, cy), (g, tcy), (tx, tcy)])
        for c in cands:
            if self.libre(c, ex):
                return c, True
        return cands[-1], False

    # -- flux de message
    def route_msg(self, el, ext, decal):
        x, y, w, h = self.shape[el]
        ex_x, ex_y, ex_w, ex_h, pos = self.ext[ext]
        cx = x + w / 2 + decal
        if pos == "dessus":
            bord, cible_y, couloir_y = y, ex_y + ex_h, self.slot[el][0] + 8
        else:
            bord, cible_y, couloir_y = y + h, ex_y, self.slot[el][1] - 8
        cands = [[(cx, bord), (cx, cible_y)]]
        for cote in (+1, -1):
            for g in self.gaps(self.col[el], cote):
                cands.append([(cx, bord), (cx, couloir_y), (g, couloir_y), (g, cible_y)])
                if pos == "dessous":  # par le haut de l'élément, pour ne pas traverser son annotation
                    haut = self.slot[el][0] + 8
                    cands.append([(cx, y), (cx, haut), (g, haut), (g, cible_y)])
        for c in cands:
            if self.libre(c, {el}):
                return c, True
        return cands[min(1, len(cands) - 1)], False

    def place_label(self, pts):
        """Nom du message : à côté d'un segment vertical, à un endroit qui ne touche ni forme, ni annotation, ni autre nom."""
        occupe = list(self.obstacles(set())) + list(self.labels.values())
        verts = sorted(((pts[k - 1], pts[k]) for k in range(1, len(pts)) if pts[k - 1][0] == pts[k][0]),
                       key=lambda sg: -abs(sg[0][1] - sg[1][1])) or [(pts[0], pts[-1])]
        for a_, b_ in verts:
            y1, y2 = sorted((a_[1], b_[1]))
            for f in (0.5, 0.3, 0.7, 0.15, 0.85, 0.05, 0.95):
                y = y1 + (y2 - y1) * f - 14
                for lx in (a_[0] + 6, a_[0] - 96):
                    b = (lx, y, 90, 28)
                    if not any(b[0] < o[0] + o[2] and o[0] < b[0] + b[2] and b[1] < o[1] + o[3] and o[1] < b[1] + b[3] for o in occupe):
                        return b
        a_, b_ = verts[0]
        return (a_[0] + 6, (a_[1] + b_[1]) / 2 - 14, 90, 28)

    def route_tout(self):
        for s, t, _ in self.m.seq:
            pts, ok = self.route_seq(s, t)
            self.edges[("seq", s, t)] = pts
            self.trace(pts, {s, t})
            if not ok:
                self.problemes.append(f"flux [{s}] → [{t}] : tracé sans croisement introuvable, à réaligner dans Camunda")
        par_el = {}
        for i, (s, t, nom) in enumerate(self.m.msg):
            el = t if s in self.m.externes else s
            par_el.setdefault(el, []).append(i)
        for el, idx in par_el.items():
            w = self.shape[el][2]
            pas = 20 if w >= 100 else 10
            decals = [0, -pas, pas, -2 * pas, 2 * pas][: len(idx)] if len(idx) > 1 else [0]
            for j, i in enumerate(idx):
                s, t, nom = self.m.msg[i]
                ext = s if s in self.m.externes else t
                pts, ok = self.route_msg(el, ext, decals[j % len(decals)])
                if s in self.m.externes:
                    pts = pts[::-1]
                self.edges[("msg", i)] = pts
                self.trace(pts, {el})
                self.labels[("msg", i)] = self.place_label(pts)
                if not ok:
                    self.problemes.append(f"message « {nom} » ([{s}] → [{t}]) : tracé sans croisement introuvable, à réaligner dans Camunda")


# ---------------------------------------------------------------- écriture XML

ISO = [(r"(\d+)\s*minutes?", "PT{}M"), (r"(\d+)\s*heures?", "PT{}H"), (r"(\d+)\s*jours?", "P{}D"),
       (r"(\d+)\s*semaines?", "P{}W"), (r"(\d+)\s*mois", "P{}M"), (r"(\d+)\s*ans?", "P{}Y")]


def iso_duree(label):
    for motif, fmt in ISO:
        mm = re.fullmatch(r"\s*" + motif + r"\s*", label.lower())
        if mm:
            return fmt.format(mm.group(1))
    return None


def a(s):
    return escape(s, {'"': "&quot;"})


def ecrire(m, p, chemin):
    L = []
    w = L.append
    w('<?xml version="1.0" encoding="UTF-8"?>')
    w('<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" '
      'xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" '
      'xmlns:di="http://www.omg.org/spec/DD/20100524/DI" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
      'id="Definitions_1" targetNamespace="http://bpmn.io/schema/bpmn" exporter="Camunda Modeler" exporterVersion="5.27.0">')
    w('  <bpmn:collaboration id="Collaboration_1">')
    for e, d in m.externes.items():
        w(f'    <bpmn:participant id="Participant_{ident(e)}" name="{a(d["name"])}" processRef="Process_{ident(e)}" />')
    w(f'    <bpmn:participant id="Participant_Interne" name="{a(m.interne or "Processus")}" processRef="Process_Interne" />')
    ref = lambda k: f"Participant_{ident(k)}" if k in m.externes else m.noeuds[k]["xid"]
    for i, (s, t, nom) in enumerate(m.msg):
        w(f'    <bpmn:messageFlow id="MsgFlow_{i + 1}_{ident(s)}_{ident(t)}" name="{a(nom)}" sourceRef="{ref(s)}" targetRef="{ref(t)}" />')
    w('  </bpmn:collaboration>')
    for e in m.externes:
        w(f'  <bpmn:process id="Process_{ident(e)}" isExecutable="false" />')
    w('  <bpmn:process id="Process_Interne" isExecutable="false">')
    w('    <bpmn:laneSet id="LaneSet_1">')
    lane_id = {ln: f"Lane_{ident(ln)}_{i + 1}" for i, ln in enumerate(m.couloirs)}
    for ln in m.couloirs:
        w(f'      <bpmn:lane id="{lane_id[ln]}" name="{a(ln)}">')
        for k in m.ordre:
            if m.noeuds[k]["lane"] == ln:
                w(f'        <bpmn:flowNodeRef>{m.noeuds[k]["xid"]}</bpmn:flowNodeRef>')
        w('      </bpmn:lane>')
    w('    </bpmn:laneSet>')
    fid = lambda s, t: f"Flow_{ident(s)}_{ident(t)}"
    for k in m.ordre:
        n = m.noeuds[k]
        nom = f' name="{a(n["label"])}"' if n["label"] else ""
        w(f'    <bpmn:{n["tag"]} id="{n["xid"]}"{nom}>')
        for s, t in n["inc"]:
            w(f'      <bpmn:incoming>{fid(s, t)}</bpmn:incoming>')
        for s, t in n["out"]:
            w(f'      <bpmn:outgoing>{fid(s, t)}</bpmn:outgoing>')
        if n["ev"] == "message":
            w(f'      <bpmn:messageEventDefinition id="MED_{ident(k)}" />')
        elif n["ev"] == "link":
            w(f'      <bpmn:linkEventDefinition id="LED_{ident(k)}" name="{a(n["label"])}" />')
        elif n["ev"] == "timer":
            iso = iso_duree(n["label"])
            if iso:
                w(f'      <bpmn:timerEventDefinition id="TED_{ident(k)}">')
                w(f'        <bpmn:timeDuration xsi:type="bpmn:tFormalExpression">{iso}</bpmn:timeDuration>')
                w('      </bpmn:timerEventDefinition>')
            else:
                w(f'      <bpmn:timerEventDefinition id="TED_{ident(k)}" />')
                m.anomalies.append(f"[{k}] minuterie « {n['label']} » sans durée chiffrée : laissée sans durée dans le fichier")
        w(f'    </bpmn:{n["tag"]}>')
    for s, t, cond in m.seq:
        nom = f' name="{a(cond)}"' if cond else ""
        w(f'    <bpmn:sequenceFlow id="{fid(s, t)}"{nom} sourceRef="{m.noeuds[s]["xid"]}" targetRef="{m.noeuds[t]["xid"]}" />')
    for k, (txt, _) in p.annot.items():
        w(f'    <bpmn:textAnnotation id="Annot_{ident(k)}"><bpmn:text>{escape(txt)}</bpmn:text></bpmn:textAnnotation>')
        w(f'    <bpmn:association id="Assoc_{ident(k)}" sourceRef="{m.noeuds[k]["xid"]}" targetRef="Annot_{ident(k)}" />')
    w('  </bpmn:process>')
    # dessin
    B = lambda b: f'<dc:Bounds x="{b[0]:g}" y="{b[1]:g}" width="{b[2]:g}" height="{b[3]:g}" />'
    WP = lambda pts: "".join(f'<di:waypoint x="{x:g}" y="{y:g}" />' for x, y in pts)
    w('  <bpmndi:BPMNDiagram id="Diagram_1">')
    w('    <bpmndi:BPMNPlane id="Plane_1" bpmnElement="Collaboration_1">')
    for e, (x, y, ww, h, _) in p.ext.items():
        w(f'      <bpmndi:BPMNShape id="Participant_{ident(e)}_di" bpmnElement="Participant_{ident(e)}" isHorizontal="true">{B((x, y, ww, h))}</bpmndi:BPMNShape>')
    w(f'      <bpmndi:BPMNShape id="Participant_Interne_di" bpmnElement="Participant_Interne" isHorizontal="true">{B((X0, p.pool_y, p.pool_w, p.pool_h))}</bpmndi:BPMNShape>')
    for ln in m.couloirs:
        w(f'      <bpmndi:BPMNShape id="{lane_id[ln]}_di" bpmnElement="{lane_id[ln]}" isHorizontal="true">{B(p.lane[ln])}</bpmndi:BPMNShape>')
    for k in m.ordre:
        n = m.noeuds[k]
        extra = ' isMarkerVisible="true"' if n["tag"] == "exclusiveGateway" else ""
        extra += ' isExpanded="false"' if n["tag"] == "subProcess" else ""
        w(f'      <bpmndi:BPMNShape id="{n["xid"]}_di" bpmnElement="{n["xid"]}"{extra}>{B(p.shape[k])}</bpmndi:BPMNShape>')
    for k, (_, b) in p.annot.items():
        w(f'      <bpmndi:BPMNShape id="Annot_{ident(k)}_di" bpmnElement="Annot_{ident(k)}">{B(b)}</bpmndi:BPMNShape>')
    for s, t, _ in m.seq:
        w(f'      <bpmndi:BPMNEdge id="{fid(s, t)}_di" bpmnElement="{fid(s, t)}">{WP(p.edges[("seq", s, t)])}</bpmndi:BPMNEdge>')
    for k, (_, b) in p.annot.items():
        x, y, ww, h = p.shape[k]
        w(f'      <bpmndi:BPMNEdge id="Assoc_{ident(k)}_di" bpmnElement="Assoc_{ident(k)}">{WP([(x + ww / 2, y + h), (x + ww / 2, b[1])])}</bpmndi:BPMNEdge>')
    for i, (s, t, nom) in enumerate(m.msg):
        mid = f"MsgFlow_{i + 1}_{ident(s)}_{ident(t)}"
        lab = p.labels.get(("msg", i))
        lab = f'<bpmndi:BPMNLabel>{B(lab)}</bpmndi:BPMNLabel>' if lab else ""
        w(f'      <bpmndi:BPMNEdge id="{mid}_di" bpmnElement="{mid}">{WP(p.edges[("msg", i)])}{lab}</bpmndi:BPMNEdge>')
    w('    </bpmndi:BPMNPlane>')
    w('  </bpmndi:BPMNDiagram>')
    for k in m.ordre:  # un plan vide par sous-processus replié, comme Camunda Modeler l'enregistre
        if m.noeuds[k]["tag"] == "subProcess":
            xid = m.noeuds[k]["xid"]
            w(f'  <bpmndi:BPMNDiagram id="Diagram_{xid}"><bpmndi:BPMNPlane id="Plane_{xid}" bpmnElement="{xid}" /></bpmndi:BPMNDiagram>')
    w('</bpmn:definitions>')
    open(chemin, "w", encoding="utf-8").write("\n".join(L) + "\n")


# ---------------------------------------------------------------- vérification d'un fichier .bpmn

NS = {"bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL", "bpmndi": "http://www.omg.org/spec/BPMN/20100524/DI",
      "dc": "http://www.omg.org/spec/DD/20100524/DC", "di": "http://www.omg.org/spec/DD/20100524/DI"}


def verifier(chemin, lignes=None):
    pb = []
    try:
        racine = ET.parse(chemin).getroot()
    except ET.ParseError as e:
        return [f"XML mal formé : {e}"], {}
    ids, tous = {}, list(racine.iter())
    for el in tous:
        i = el.get("id")
        if i:
            if i in ids:
                pb.append(f"id en double : {i}")
            ids[i] = el
            if not re.match(r"^[A-Za-z_][\w.-]*$", i):
                pb.append(f"id invalide : {i}")
    for el in tous:
        for att in ("sourceRef", "targetRef", "processRef", "bpmnElement"):
            v = el.get(att)
            if v and v not in ids:
                pb.append(f"{att}=\"{v}\" ne pointe vers aucun id")
        if el.tag.endswith("flowNodeRef") or el.tag.endswith("incoming") or el.tag.endswith("outgoing"):
            if (el.text or "").strip() not in ids:
                pb.append(f"référence {el.text} introuvable")
    loc = lambda e: e.tag.split("}")[1]
    noeud = lambda t: t.endswith("Task") or t.endswith("Event") or t.endswith("Gateway") or t == "subProcess"
    shapes, edges = {}, {}
    for s in racine.iter(f"{{{NS['bpmndi']}}}BPMNShape"):
        b = s.find("dc:Bounds", NS)
        shapes[s.get("bpmnElement")] = tuple(float(b.get(k)) for k in ("x", "y", "width", "height"))
    for e in racine.iter(f"{{{NS['bpmndi']}}}BPMNEdge"):
        edges[e.get("bpmnElement")] = [(float(w.get("x")), float(w.get("y"))) for w in e.findall("di:waypoint", NS)]
    for i, el in ids.items():
        t = loc(el)
        if (noeud(t) or t in ("participant", "lane", "textAnnotation")) and i not in shapes:
            pb.append(f"{i} n'a pas de forme dans le dessin")
        if t in ("sequenceFlow", "messageFlow", "association") and i not in edges:
            pb.append(f"{i} n'a pas de trait dans le dessin")
    formes = {i: b for i, b in shapes.items() if i in ids and (noeud(loc(ids[i])) or loc(ids[i]) == "textAnnotation")}
    ov = lambda p, q: p[0] < q[0] + q[2] and q[0] < p[0] + p[2] and p[1] < q[1] + q[3] and q[1] < p[1] + p[3]
    cles = list(formes)
    for x in range(len(cles)):
        for y in range(x + 1, len(cles)):
            if ov(formes[cles[x]], formes[cles[y]]):
                pb.append(f"formes superposées : {cles[x]} / {cles[y]}")
    for ln in racine.iter(f"{{{NS['bpmn']}}}lane"):
        lb = shapes.get(ln.get("id"))
        for r in ln.findall("bpmn:flowNodeRef", NS):
            b = shapes.get((r.text or "").strip())
            if lb and b and not (b[0] >= lb[0] and b[1] >= lb[1] and b[0] + b[2] <= lb[0] + lb[2] and b[1] + b[3] <= lb[1] + lb[3]):
                pb.append(f"{r.text} sort de son couloir « {ln.get('name')} »")
    for i, pts in edges.items():
        el = ids.get(i)
        if el is None:
            continue
        s, t = el.get("sourceRef"), el.get("targetRef")
        for b, p, nom in ((shapes.get(s), pts[0], s), (shapes.get(t), pts[-1], t)):
            if b and not (b[0] - 3 <= p[0] <= b[0] + b[2] + 3 and b[1] - 3 <= p[1] <= b[1] + b[3] + 3):
                pb.append(f"{i} ne touche pas {nom}")
        if loc(el) == "association":
            continue
        for k in range(1, len(pts)):
            if pts[k][0] != pts[k - 1][0] and pts[k][1] != pts[k - 1][1]:
                pb.append(f"{i} a un segment en biais")
            for fid, b in formes.items():
                if fid in (s, t):
                    continue
                if Plan.coupe(pts[k - 1], pts[k], b):
                    pb.append(f"{i} traverse {fid}")
                    break
    segs = {}
    for i, pts in edges.items():
        if i in ids and loc(ids[i]) in ("sequenceFlow", "messageFlow"):
            segs[i] = [(pts[k - 1], pts[k]) for k in range(1, len(pts))]
    cl = list(segs)
    for x in range(len(cl)):
        for y in range(x + 1, len(cl)):
            for (p1, p2) in segs[cl[x]]:
                for (q1, q2) in segs[cl[y]]:
                    if p1[0] == p2[0] == q1[0] == q2[0]:
                        lo = max(min(p1[1], p2[1]), min(q1[1], q2[1]))
                        hi = min(max(p1[1], p2[1]), max(q1[1], q2[1]))
                        if hi - lo > 5 and not set(ids[cl[x]].get(a_) for a_ in ("sourceRef", "targetRef")) & set(ids[cl[y]].get(a_) for a_ in ("sourceRef", "targetRef")):
                            pb.append(f"traits superposés : {cl[x]} / {cl[y]}")
    stats = {"éléments": sum(1 for el in ids.values() if noeud(loc(el))), "participants": sum(1 for el in ids.values() if loc(el) == "participant"),
             "flux de séquence": sum(1 for el in ids.values() if loc(el) == "sequenceFlow"),
             "flux de message": sum(1 for el in ids.values() if loc(el) == "messageFlow"),
             "annotations": sum(1 for el in ids.values() if loc(el) == "textAnnotation")}
    if lignes is not None:
        noms = {el.get("id"): el.get("name") or "" for el in ids.values()}
        for l in lignes:
            if l["type"].strip().lower() == "participant externe":
                if f"Participant_{ident(l['id'])}" not in ids:
                    pb.append(f"ligne [{l['id']}] absente du fichier")
                continue
            xid = "E_" + ident(l["id"])
            if xid not in ids:
                pb.append(f"ligne [{l['id']}] absente du fichier")
            elif (l["label"] if l["label"] not in NONE else "") != noms[xid]:
                pb.append(f"[{l['id']}] libellé différent du tableau")
    return list(dict.fromkeys(pb)), stats


# ---------------------------------------------------------------- programme

def main(argv):
    if len(argv) == 3 and argv[1] == "--verifier":
        pb, st = verifier(argv[2])
        print(f"Vérification de {argv[2]} : " + ", ".join(f"{v} {k}" for k, v in st.items()))
        print("Problèmes : " + ("aucun" if not pb else "\n- " + "\n- ".join(pb)))
        return 1 if pb else 0
    if len(argv) != 3:
        print(__doc__)
        return 2
    lignes, questions = lire_livrable(argv[1])
    if not lignes:
        print("Tableau du processus introuvable dans le livrable : rien n'a été produit.")
        return 2
    m = Modele(lignes, questions)
    p = Plan(m)
    ecrire(m, p, argv[2])
    pb, st = verifier(argv[2], [l for l in lignes if l["type"].strip().lower() in TYPES])
    print(f"Fichier écrit : {argv[2]}")
    print("Contenu : " + ", ".join(f"{v} {k}" for k, v in st.items()))
    anomalies = m.anomalies + p.problemes + pb
    print("Anomalies du tableau non corrigées et points à reprendre dans Camunda : " + ("Aucune" if not anomalies else "\n- " + "\n- ".join(anomalies)))
    return 1 if anomalies else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
