#!/bin/sh

RESET="\033[0m"

BLACK="\033[0;30m"
RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"

BOLD_RED="\033[1;31m"
BOLD_GREEN="\033[1;32m"
BOLD_YELLOW="\033[1;33m"
BOLD_CYAN="\033[1;36m"

BRIGHT_BLACK="\033[0;90m"
BRIGHT_RED="\033[0;91m"
BRIGHT_GREEN="\033[0;92m"
BRIGHT_YELLOW="\033[0;93m"

BOLD_BRIGHT_RED="\033[1;91m"
BOLD_BRIGHT_GREEN="\033[1;92m"
BOLD_BRIGHT_YELLOW="\033[1;93m"

POSITIONAL_ARGS=( )

while [[ $# -gt 0 ]]; do
    case $1 in
        -i|--ip)
            IP="$2"
            shift
            shift
            ;;
        -u|--username)
            USERNAME="$2"
            shift
            shift
            ;;
        -p|--password)
            PASSWORD="$2"
            shift
            shift
            ;;
        -i=*|--ip=*)
            IP="${1#*=}"
            shift
            ;;
        -u=*|--username=*)
            USERNAME="${1#*=}"
            shift
            ;;
        -p=*|--password=*)
            PASSWORD="${1#*=}"
            shift
            ;;
        -*|--*)
            echo "Unknown option $1"
            exit 1
            ;;
        *)
            POSITIONAL_ARGS+=("$1")
            shift
            ;;
    esac
done

set -- "${POSITIONAL_ARGS[@]}"

if [[ $IP == "" ]]; then
    if [[ $USERNAME != "" && $PASSWORD != "" ]]; then
        echo "${BOLD_RED}IP not provided! Using default: ${BOLD_BRIGHT_YELLOW}10.27.33.19${BOLD_RED}"
    else
        echo "${BOLD_RED}IP not provided!       Using default: ${BOLD_BRIGHT_YELLOW}10.27.33.19${BOLD_RED}"
    fi
    IP="10.27.33.19"
fi

if [[ $USERNAME == "" ]]; then
    echo "${BOLD_RED}Username not provided! Using default: ${BOLD_BRIGHT_YELLOW}pi${BOLD_RED}"
    USERNAME="pi"
fi

if [[ $PASSWORD == "" ]]; then
    echo "${BOLD_RED}Password not provided! Using default: ${BOLD_BRIGHT_YELLOW}raspberry${BOLD_RED}"
    PASSWORD="raspberry"
fi

DEST="$USERNAME@$IP:/etc/piled/custom_effects/"
echo "${BRIGHT_BLACK}Copying files to $DEST${RESET}"

scp ../pi/custom_effects/* $DEST
