# FacturePro MCP Server

Electronic invoice processing & compliance (Peppol, Chorus Pro)

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
- ✅ Peppol Access Point
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

## 📊 Comparaison Détaillée

| Fonctionnalité | Lite (Gratuit) | Solo (€1,500) | Pro (€2,500/an) |
|----------------|-----------------|---------------------|---------------------|
| **Performance** | 1x baseline | 10x | 30x |
| **Parsing PDF** | ✅ | ✅ | ✅ |
| **Validation TVA** | Basique | Standard | Avancée |
| **Exports** | 2 formats | 5 formats | 7+ formats |
| **Batch** | ❌ | 20 factures | 100+ factures |
| **Peppol Access Point** | ❌ | ❌ | ✅ |
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
- ✅ Besoin de Peppol Access Point
- ✅ Support prioritaire important
- ✅ 100+ factures par mois
- ✅ Besoin de conformité multi-pays

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

---

## 🏢 About IA Business Booster

[AI-powered automation for European SMEs](https://www.iabusinessbooster.be)

---

**Note:** This repository contains the Lite version only.
Solo and Pro versions include additional features and support.

See [Pricing](https://www.iabusinessbooster.be/mcp-portfolio.html) for details.
