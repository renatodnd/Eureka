#!/bin/bash
# Script: setup_venv.sh
# Descrição: Cria um ambiente virtual Python e instala dependências do requirements.txt

# Faz o script parar se algum comando falhar
set -e

# Nome do ambiente virtual (padrão: venv)
VENV_DIR="venv"

# Verifica se o Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 não encontrado. Instale o Python 3 antes de continuar."
    exit 1
fi

# Cria o ambiente virtual
echo "🐍 Criando ambiente virtual em '$VENV_DIR'..."
python3 -m venv "$VENV_DIR"

# Ativa o ambiente virtual
echo "⚙️  Ativando ambiente virtual..."
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

# Verifica se o arquivo requirements.txt existe
if [ -f "requirements.txt" ]; then
    echo "📦 Instalando dependências do requirements.txt..."
    pip install --upgrade pip
    pip install -r requirements.txt
    echo "✅ Dependências instaladas com sucesso!"
else
    echo "⚠️  Nenhum arquivo requirements.txt encontrado. Ambiente criado sem dependências."
fi

echo "🎉 Ambiente virtual pronto! Para ativar manualmente, use:"
echo "source $VENV_DIR/bin/activate"
