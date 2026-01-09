# FacturePro MCP Server

Electronic invoice processing & compliance (Peppol, Chorus Pro)

> **⚠️ Important Clarification:** FacturePro excels at **RECEIVING** and **PROCESSING** Peppol invoices. For **SENDING** Peppol invoices, see the [Émission Peppol](#-mission-factures-peppol) section below.

## 🎯 3 Éditions pour Chaque Usage

### 🆓 LITE (Gratuit - Open Source)

**Pour qui :** Test, évaluation, petits volumes

**Caractéristiques :**
- PDF parsing
- Basic validation
- Format conversion
- Performance : Baseline (1x)
- Support : Communauté (GitHub issues)
- Usage : Illimité (personnel)
- Documentation : Public docs

**Install:**
```bash
pip install facturepro-mcp
python -m facturepro_mcp
```

---

### 👤 SOLO (One-Time - €1,500)

**Pour qui :** Freelances comptables, TPE 1-2 personnes

**Caractéristiques :**
- ✅ **Licence perpétuelle** (pas d'expiration)
- ✅ Performance : 10x vs Lite
- ✅ Fonctions : 7 exports comptables
- ✅ Support : 30 jours (email)
- ✅ Utilisateurs : 1 seul
- ✅ Updates : 1 an inclus

**Prix :** €1,500 ONE-TIME

**Install:**
```bash
pip install facturepro-mcp
export IABB_LICENSE_KEY="IABB-XXXXX-XXXXX-XXXXX"
python -m facturepro_mcp
```

---

### 🏆 PRO (Annuel - €2,500/an)

**Pour qui :** Cabinets comptables 3-10 personnes, PME

**Caractéristiques :**
- ✅ **Licence annuelle** (renouvellement auto)
- ✅ Performance : 30x vs Lite
- ✅ Fonctions : TOUTES + Signal Loop
- ✅ **Peppol RECEPTION** (parse XML UBL, validation)
- ✅ Auto-réparation factures
- ✅ Batch 100+ factures
- ✅ Validation TVA avancée
- ✅ Support : Prioritaire illimité
- ✅ Updates : Automatiques inclus
- ✅ SLA : 99% uptime
- ✅ Utilisateurs : Jusqu'à 5

**Prix :** €2,500/an

**Install:**
```bash
pip install facturepro-mcp facturepro-core-pro
export IABB_LICENSE_KEY="IABB-YYYYY-YYYYY-YYYYY"
python -m facturepro_mcp
```

---

### 🚀 PRO + SEND (Annuel - €3,500/an) ⭐

**Pour qui :** Cabinets comptables et PME nécessitant l'émission Peppol

**Caractéristiques (PRO + Émission) :**
- ✅ **TOUTES les fonctionnalités PRO**
- ✅ **Tool `sendpeppol` intégré** (envoi automatique)
- ✅ **B2B Router API setup** (Access Point gratuit)
- ✅ **Génération UBL automatique**
- ✅ **Conformité Peppol 2026 complète** (réception + émission)
- ✅ Support prioritaire émission
- ✅ Tests sandbox inclus

**Prix :** €3,500/an (PRO €2,500 + Send Addon €1,000)

**Install:**
```bash
pip install facturepro-mcp facturepro-core-pro facturepro-send-addon
export IABB_LICENSE_KEY="IABB-ZZZZZ-ZZZZZ-ZZZZZ"
python -m facturepro_mcp
```

---

##  Comparaison Détaillée

| Fonctionnalité | Lite (Gratuit) | Solo (€1,500) | Pro (€2,500/an) |
|----------------|-----------------|---------------------|---------------------|
| **Performance** | 1x baseline | 10x | 30x |
| **Parsing PDF** | ✅ | ✅ | ✅ |
| **Validation TVA** | Basique | Standard | Avancée |
| **Exports** | 2 formats | 5 formats | 7+ formats |
| **Batch** | ❌ | 20 factures | 100+ factures |
| **Peppol RÉCEPTION** | ✅ Basique | ✅ Standard | ✅ Complet |
| **Peppol ÉMISSION** | ❌ | ❌ | ❌ |
| **Peppol ÉMISSION (Pro+Send)** | ❌ | ❌ | ✅ |
| **Auto-réparation** | ❌ | ❌ | ✅ |
| **Détection anomalies** | ❌ | ❌ | ✅ |
| **Compliance multi-pays** | ❌ | ❌ | ✅ |
| **Support** | Communauté | 30 jours email | Prioritaire illimité |
| **Updates** | Public | 1 an inclus | Auto inclus |
| **SLA** | ❌ | ❌ | 99% uptime |
| **Utilisateurs** | 1 | 1 | Jusqu'à 5 |

---

## 🚀 Quick Start (Lite)

1. **Install:**
```bash
pip install facturepro-mcp
```

2. **Configure Claude Desktop:**
```json
{
  "mcpServers": {
    "facturepro_mcp": {
      "command": "python",
      "args": ["-m", "facturepro_mcp"]
    }
  }
}
```

3. **Restart Claude Desktop**

4. **Use in Claude:**
```
Please use FacturePro to process this invoice...
```

---

## 💰 Pour Choisir Votre Édition

**Choisissez LITE si :**
- ✅ Vous voulez tester gratuitement
- ✅ Usage personnel ou petit volume
- ✅ Pas besoin de support prioritaire
- ✅ Quelques factures par mois

**Choisissez SOLO si :**
- ✅ Vous êtes freelance comptable
- ✅ TPE 1-2 personnes
- ✅ Vous préférez un paiement unique
- ✅ Licence perpétuelle importante
- ✅ 20-50 factures par mois

**Choisissez PRO si :**
- ✅ Cabinet comptable 3-10 personnes
- ✅ PME avec comptabilité interne
- ✅ Besoin de **RÉCEPTION** Peppol (parse XML, validation)
- ✅ Support prioritaire important
- ✅ 100+ factures par mois
- ✅ Besoin de conformité multi-pays

**Choisissez PRO + SEND si :**
- ✅ Cabinet comptable 3-10 personnes
- ✅ PME avec comptabilité interne
- ✅ Besoin de **RÉCEPTION + ÉMISSION** Peppol complètes
- ✅ Obligation Peppol 2026 (envoyer factures)
- ✅ Solution tout-en-un (pas d'AP externe)
- ✅ Support prioritaire émission
- ✅ 100+ factures par mois
- ✅ Conformité multi-pays

---

## 💡 ROI Calculé

### Scénario Solo : Freelance Comptable
- **Temps gagné :** 6h/semaine
- **Taux horaire :** €50/h
- **Économie :** 6h × €50 × 52 sem = €15,600/an
- **Investissement :** €1,500 one-time
- **ROI :** 10.4x la première année

### Scénario Pro : Cabinet 5 Comptables
- **Temps gagné :** 20h/semaine (5 personnes × 4h)
- **Coût horaire moyen :** €60/h
- **Économie :** 20h × €60 × 52 sem = €62,400/an
- **Investissement :** €2,500/an
- **ROI :** 25x

---

## 📥 Réception Factures Peppol

FacturePro excelle dans le traitement des factures **ENTRANTES** :

✅ **`extractpeppolxml`** : Parse XML UBL Peppol reçus
✅ **`parsepdfinvoice`** : OCR PDF + validation
✅ **`converttoaccounting`** : Écritures PCMN belges
✅ **`exporttosoftware`** : Export 7 logiciels comptables
✅ **Validation** : Peppol BIS 3.0, multi-pays TVA
✅ **Auto-réparation** : Correction automatique erreurs

**Workflow Réception :**
```
Fournisseur → Réseau Peppol → Votre AP → FacturePro (parse/validate/export)
```

---

## 📤 Émission Factures Peppol

Pour **ÉMETTRE** des factures Peppol (obligatoire 2026), utilisez un Access Point certifié :

### Option 1 : B2B Router (Recommandé - Gratuit)

**Avantages :**
- ✅ 100% gratuit, illimité
- ✅ API simple et documentée
- ✅ Conformité certifiée Peppol
- ✅ Support en français
- ✅ Intégration rapide (2h)

**URL :** https://www.b2brouter.net/be/peppol-gratuit/

**Workflow :**
```
1. Signup gratuit sur B2B Router
2. Obtenez API key
3. FacturePro génère UBL XML (via models)
4. Envoyez UBL via B2B Router API
5. Destinataire reçoit via son AP Peppol
```

**Exemple Code :**
```python
import requests

# Générer UBL avec FacturePro
ubl_xml = facturepro.generate_ubl(invoice_data)

# Envoyer via B2B Router
response = requests.post(
    "https://api.b2brouter.net/v1/peppol/send",
    headers={"Authorization": f"Bearer {B2B_API_KEY}"},
    json={
        "document": ubl_xml,
        "recipient_id": "BE0123456789",
        "recipient_scheme": "0208",  # BE VAT
        "document_type": "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
    }
)

transmission_id = response.json()["transmission_id"]
```

### Option 2 : Accountable (Gratuit pour TPE)

**Avantages :**
- ✅ Gratuit pour TPE (<25 factures/mois)
- ✅ Interface user-friendly
- ✅ Support Peppol natif

**URL :** https://www.accountable.eu

### Option 3 : FacturePro Pro + Send (Addon) ⭐

**Solution intégrée** avec tool `sendpeppol` inclus.

**Pricing** : +€1,000/an addon

**Inclus :**
- ✅ Tool `sendpeppol` (envoi automatique)
- ✅ B2B Router API setup
- ✅ Génération UBL automatique
- ✅ Support prioritaire émission
- ✅ Tests sandbox inclus

**Contact** : mcp@iabusinessbooster.be

### Workflow Complet (Réception + Émission)

```
┌─────────────────────────────────────────────────────────────┐
│                     RÉCEPTION (PRO)                         │
├─────────────────────────────────────────────────────────────┤
│ Fournisseur → Peppol → AP → FacturePro → Export Comptable   │
│                                                             │
│ ✅ extractpeppolxml  ✅ parsepdfinvoice                     │
│ ✅ converttoaccounting  ✅ exporttosoftware                 │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                     ÉMISSION (Pro+Send)                     │
├─────────────────────────────────────────────────────────────┤
│ Facture → FacturePro → UBL → B2B Router → Peppol → Client  │
│                                                             │
│ ✅ generate_ubl  ✅ sendpeppol  ✅ B2B Router API          │
└─────────────────────────────────────────────────────────────┘
```

---

## 🏢 Obtenir une Licence Solo ou Pro

### Option 1 : Direct

**Contact :** mcp@iabusinessbooster.be
**Site web :** https://www.iabusinessbooster.be

### Option 2 : Formulaire

1. Visitez : https://www.iabusinessbooster.be/contact
2. Remplissez le formulaire (1 minute)
3. Recevez votre devis sous 24h
4. Signez électroniquement
5. Recevez votre licence immédiatement

### Option 3 : Bundles Multi-MCP

**Bundle Starter (3 MCP) :**
- Solo : €3,900 (vs €4,500 séparés)
- Pro : €6,500/an ou €575/mois

**Bundle Business (5 MCP) :**
- Solo : €6,500 (vs €7,500 séparés)
- Pro : €11,000/an ou €975/mois
- Pro + Send : €12,500/an ou €1,075/mois

**Voir :** https://www.iabusinessbooster.be/mcp-portfolio.html

---

## 📚 Documentation

- **[Full API Docs](https://www.iabusinessbooster.be/docs/facturepro-mcp)**
- **[Pricing Details](https://www.iabusinessbooster.be/mcp-portfolio.html)**
- **[Installation Guide](https://www.iabusinessbooster.be/docs/facturepro-mcp/install)**
- **[Examples](https://github.com/IA-Business-Booster/facturepro-mcp/tree/main/examples)**

---

## 🤝 Contributing

Contributions welcome! This is the open-source Lite version.

For Pro features, contact us directly.

---

## 📄 License

- **Lite:** MIT License (free, open-source)
- **Solo:** Commercial license (perpetual)
- **Pro:** Commercial license (annual)
- **Pro + Send:** Commercial license (annual) includes sendpeppol addon

---

## 🏢 About IA Business Booster

[AI-powered automation for European SMEs](https://www.iabusinessbooster.be)

---

**Note:** This repository contains the Lite version only.
Solo and Pro versions include additional features and support.

**Peppol Compliance:** FacturePro PRO handles Peppol RECEPTION (parsing, validation, export). For Peppol EMISSION, use B2B Router (free) or upgrade to PRO + SEND addon.

See [Pricing](https://www.iabusinessbooster.be/mcp-portfolio.html) for details.
