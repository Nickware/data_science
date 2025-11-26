# HUGO + GitHub + Visual Studio Code

Cómo conectar **HUGO + GitHub + Visual Studio Code** para crear un flujo de trabajo perfecto para una bitácora.

## **1. Configuración Inicial Integrada**

### **Instalación de Prerrequisitos**

```bash
# Instalar HUGO (extended version)
# Windows: choco install hugo-extended
# Ubuntu: snap install hugo
# macOS: brew install hugo

# Verificar instalación
hugo version

# Instalar Git
git --version
```

### **Configurar Git Globalmente**
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@empresa.com"
git config --global init.defaultBranch main
```

---

## **2. Crear Proyecto HUGO Integrado**

### **En VSCode:**
1. Abrir terminal integrado (`` Ctrl+` ``)
2. Ejecutar:

```bash
# Crear nuevo sitio HUGO
hugo new site bitacora-red
cd bitacora-red

# Inicializar Git
git init

# Agregar tema (ejemplo con Docsy)
git submodule add https://github.com/google/docsy.git themes/docsy
```

### **Configurar HUGO**
```hugo.toml
baseURL = 'https://tusuario.github.io/bitacora-red/'
languageCode = 'es-es'
title = 'Bitácora de Red Local'
theme = 'docsy'

[params]
  description = 'Documentación técnica de infraestructura de red'

[menu]
  [[menu.main]]
    name = "Servidores"
    url = "/servidores/"
    weight = 10
  [[menu.main]]
    name = "Switches"
    url = "/switches/"
    weight = 20
```

---

## **3. Configurar VSCode Optimizado**

### **Extensions Recomendadas:**
- **Hugo Language and Syntax Support**
- **Markdown All in One**
- **GitLens** (para mejor control de Git)
- **Prettier** (formateo automático)
- **Auto-Open Markdown Preview**

### **Configuración de Workspace (`.vscode/settings.json`):**
```json
{
  "files.associations": {
    "*.md": "markdown"
  },
  "emmet.includeLanguages": {
    "markdown": "html"
  },
  "[markdown]": {
    "editor.wordWrap": "on",
    "editor.quickSuggestions": true
  },
  "markdown.preview.breaks": true,
  "git.autofetch": true,
  "git.confirmSync": false
}
```

### **Snippets Personalizados (`.vscode/hugo.code-snippets`):**
```json
{
  "Hugo Front Matter": {
    "prefix": "hugo-fm",
    "body": [
      "---",
      "title: \"${1:Título}\"",
      "date: \"${CURRENT_YEAR}-${CURRENT_MONTH}-${CURRENT_DATE}\"",
      "description: \"${2:Descripción}\"",
      "tags: [${3:tag1, tag2}]",
      "draft: false",
      "---",
      "",
      "${4:## Introducción}",
      ""
    ],
    "description": "Front matter para HUGO"
  }
}
```

---

## **4. Flujo de Trabajo en VSCode**

### **Estructura de Carpetas en VSCode:**
```
BITACORA-RED/ (Workspace en VSCode)
├── .github/
│   └── workflows/
│       └── deploy.yml    # CI/CD
├── archetypes/
├── content/
│   ├── servidores/
│   │   ├── _index.md
│   │   └── servidor-prod.md
│   └── switches/
├── static/
│   └── images/
├── themes/
│   └── docsy/ (submodule)
└── hugo.toml
```

### **Crear Nuevo Contenido:**
1. **Terminal de VSCode:**
```bash
hugo new servidores/nuevo-servidor.md
```

2. **Editar en VSCode con preview:**
   - Abre el archivo `.md`
   - `Ctrl+Shift+V` para preview Markdown
   - Usa los snippets personalizados

### **Ejemplo de Archivo de Contenido:**
```markdown
---
title: "Servidor WEB-PROD"
date: 2024-03-20T10:00:00Z
description: "Servidor web de producción"
tags: ["servidor", "apache", "producción"]
draft: false
---

## Especificaciones Técnicas

- **IP**: 192.168.1.50
- **SO**: Ubuntu Server 22.04
- **CPU**: 4 vCPUs
- **RAM**: 8GB

## Configuración

```bash
# Ejemplo de configuración
sudo systemctl status apache2
```

## Historial de Mantenimiento

| Fecha      | Cambio              | Responsable |
| ---------- | ------------------- | ----------- |
| 2024-03-20 | Instalación inicial | Admin       |
```

---

## **5. Configuración de GitHub**

### **Crear Repositorio:**
1. Ve a GitHub.com → New Repository
2. Nombre: `bitacora-red`
3. **NO inicializar con README** (ya tenemos contenido local)

### **Conectar Repositorio Local:**
```bash
# En terminal de VSCode:
git remote add origin https://github.com/tuusuario/bitacora-red.git
git branch -M main
git push -u origin main
```

### **Configurar GitHub Pages:**
1. En repositorio → **Settings** → **Pages**
2. **Source**: GitHub Actions
3. **Branch**: `gh-pages` (se creará automáticamente)

---

## **6. Automatización con GitHub Actions**

### **Crear Workflow (`.github/workflows/deploy.yml`):**
```yaml
name: Deploy HUGO to GitHub Pages

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: true
          fetch-depth: 0

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: 'latest'
          extended: true

      - name: Build
        run: hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v4
        if: github.ref == 'refs/heads/main'
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
          force_orphan: true
```

---

## **7. Flujo de Trabajo Completo**

### **Día a día en VSCode:**

1. **Sincronizar cambios:**
```bash
git pull origin main
```

2. **Crear nueva entrada:**
```bash
hugo new switches/nuevo-switch.md
```

3. **Editar en VSCode:**
   - Usa preview Markdown
   - Aprovecha snippets
   - Previsualiza local: `hugo server -D`

4. **Probar localmente:**
```bash
hugo server -D
# Ver en: http://localhost:1313
```

5. **Commit y push:**
```bash
git add .
git commit -m "docs: agregado nuevo switch Cisco 2960"
git push origin main
```

### **Comandos Útiles en Terminal VSCode:**
```bash
# Servidor desarrollo con drafts
hugo server -D --disableFastRender

# Build producción
hugo --minify

# Ver estado Git
git status

# Sincronizar tema
git submodule update --remote
```

---

## **8. Estructura de Commits Recomendada**

```bash
git commit -m "feat: nuevo servidor de base de datos"
git commit -m "docs: actualizada IP switch core"
git commit -m "fix: corrección en procedimiento backup"
```

---

## **9. URLs Resultantes**

- **Local**: `http://localhost:1313` (desarrollo)
- **GitHub Pages**: `https://tusuario.github.io/bitacora-red/`
- **Red Local**: Puedes clonar el repositorio `gh-pages` y servir localmente

---

## **10. Script de Automatización (opcional)**

Crear un script `deploy.sh` en la raíz:
```bash
#!/bin/bash
echo "▶️ Iniciando deploy..."
hugo --minify
git add .
git commit -m "deploy: $1"
git push origin main
echo "✅ Deploy completado!"
```

Uso en VSCode terminal: `./deploy.sh "agregado nuevo equipo"`

---

**¡Con se tiene un flujo profesional!** Cada vez que se haga `git push` desde VSCode, GitHub Actions generará automáticamente el sitio estático y lo publicará en GitHub Pages. El equipo puede colaborar mediante pull requests y todo queda versionado.