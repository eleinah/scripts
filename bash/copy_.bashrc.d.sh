# This script copies everything from ~/git/dotfiles/.bashrc.d/ to my FCOS hosts via scp

SOURCE_PATH="/home/$USER/git/dotfiles/.bashrc.d/"
DEST_PATH="~/"

HOSTS=(media bunker util storage)

for HOST in "${HOSTS[@]}"; do
    scp -r "$SOURCE_PATH" "$HOST:$DEST_PATH"
    ssh "$HOST" "source ~/.bashrc"
done
