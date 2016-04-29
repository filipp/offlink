### Introduction

This tool synchronizes shared folders for offline editing. It may come in useful if you have some folders on a file server that you would like to "take with you" - you then simply drag those folders to

It has 3 modes of operation:

- Dragging new folder: create "link" between source and target and sync
- Dragging previously synced folder: "unlink" source and target
- Launch without drag/drop: sync folders

### How to

- Drag your source items onto the Offlink droplet
- Run the Offlink droplet before you go "offline"
- To remove items from the "linked list", just drag the source file/folders onto it again

### Bugs

It would be nice to be able to sync files back to the source directory as well and the rsync code is in there, but I don't know how to trigger that behaviour (alt-clicking would be an option, but stock AppleScript cannot detect that).

### License

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

     Copyright (C) 2016 Filipp Lepalaan <filipp@mac.com>

     Everyone is permitted to copy and distribute verbatim or modified
     copies of this license document, and changing it is allowed as long
     as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

    0. You just DO WHAT THE FUCK YOU WANT TO.
