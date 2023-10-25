# flake-ift511-labo2

Ce répetoire vise à fournir un environnement de développement reproductible à
l'aide du `nix package manager` pour le labo2 dans le cadre du cours IFT511.

## Plateformes supportées

Les plateformes suivantes sont supportées par:

- MacOS (ARM et x86_64)
- Linux (ARM et x86_64)
- WSL2 (ARM et x86_64)

**Note importante**: Bien que toutes ces plateformes soient supportées, il est
à noter que seule la plateforme Linux x86_64 a été testée, car c'est l'OS que
j'utilise personnellement. Cependant, l'environnement de développement devrait
fonctionner correctement sur toutes les autres plateformes mentionnées.

## Qu'est-ce que nix et pourquoi l'utiliser?

[Nix](https://nixos.org/) est un gestionnaire de paquets et un système de configuration
révolutionnaire qui sert à créer des environnements de développement et des
builds de manière reproductible et déterministe. Cela garantit que les systèmes
fonctionnent de manière fiable, éliminant ainsi les "ça fonctionne sur ma machine"
et les problèmes de dépendance.

Nix permet également l'installation en cache des applications sans apporter de
modifications à l'état global du système. Plus de détails sont disponibles dans la
documentation officielle, mais cela dépasse la portée de ce répertoire.

## Installation de nix-installer

Vous pouvez installer `nix-installer` depuis [ce répertoire GitHub](https://github.com/DeterminateSystems/nix-installer).
Pour plus d'informations, veuillez consulter le lien.

Cette distribution est recommandée puisqu'elle vous permet d'installer `nix` avec
le support pour les `flakes` sans configuration externe.

- **Utilisateurs Linux**: Assurez-vous que votre distribution utilise `systemd`.
- **Utilisateurs MacOS**: Assurez-vous d'être login à MacOS via l'interface
  graphique avant de procéder à l'installation.
- **Utilisateurs WSL2**: Vous devez avoir activé `systemd` pour WSL2 avant de procéder
  à l'installation.

### Installation nix

Installez le `nix package manager` avec la commande suivante:

```bash
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
```

## Setup environnement de développement

Pour commencer, veuillez cloner ce répertoire avec la commande suivante:

```bash
git clone https://github.com/gcleroux/flake-ift511-labo2
```

Par la suite, vous pouvez `cd` dans le répertoire:

```bash
cd flake-ift511-labo2
```

### Utilisation du flake.nix pour l'environnement de développement (devShell)

Le fichier `flake.nix` fourni est utilisé pour configurer l'environnement de
développement (`devShell`). Vous pouvez ainsi vous assurer que toutes les dépendances
nécessaires sont correctement installées et configurées pour le exécuter le
code du labo2 sur tous les environnements supportés.

Pour utiliser l'environnement de développement, utilisez la commande suivante
à partir de la racine du répertoire:

```bash
nix develop
```

Cette commande installe en cache les dépendances nécessaires pour l'exécution
du labo et active une `shell` bash temporaire dans laquelle vous pouvez tester
votre code.

---

N'hésitez pas à consulter les documentations et les liens fournis pour plus
d'informations et de détails sur chaque étape.
