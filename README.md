# Invicta
*Team Fortress 2 custom configuration files, launch options and mod recommendations. Used in conjunction with [mastercomfig](https://mastercomfig.com/).*

## Launch Options
```
-novid -nojoy -nosteamcontroller -nohltv -particles 1 -precachefontchars -noquicktime
```

## Installation
Click [Here](https://github.com/AdImperiumTe/Invicta/archive/refs/heads/master.zip) for the latest config release.  
Extract the ZIP file, Copy and Paste the folders contents into `tf\cfg`, found in the `Team Fortress 2` folder.  
Inside `tf\cfg` should be the folders `overrides` and `user`.

### Find Team Fortress 2 Folder

In `Steam` go to `Library` and find `Team Fortress 2`, right-click it and select `Manage` > `Browse local files`.  
This will open up your `Team Fortress 2` folder.

## Config Features
* **Mod Key:** Used in conjunction with another key (default key: `CTRL`) for more keyboard functionality.
* **Wait Tester:** Checks to see if the server has the wait command enabled.
* **Interp:** Sets the interp for different classes based on if they use projectiles or not.
* **Auto Crouch-Jump:** Automatically crouch-jump when pressing spacebar.
* **Netgraph:** Provides you with info such as latency (ping in ms), server speeds, fps, interpolation and tickrate when you have pressed the `TAB` key.
* **Viewmodel Toggler:** Toggles the display of the active weapons' viewmodel by pressing the `DELETE` key.
* **Class Switcher:** Uses a Modkey and keys 1 through 9 to quickly switch class.
* **Loutout Switcher:** Uses the Modkey and arrow keys to switch loadouts.
* **Medic/Über Switcher:** Switches between calling for either a Medic or Übercharge when `modKey` has been pressed down or not (default key: `E` to call).
* **Null Cancelling Movement:** Lets you immediately change direction.

## Class Specific Features
* **Scout: Secondary Weapon Toggle:** Allows the Scout to quickly throw the secondary weapon (e.g. mad milk), or switch to the winger for a greater jump height.
* **Soldier: Rocket Jump:** A simple rocket jump script that doesn't use the wait command but still provides a decent jump. Jump script bound to `MOUSE2` when toggled on (use `R` to toggle).
* **Engineer: Eureka Effect Teleport:** Press `Q` to go to spawn. Hold `CTRL` and Press `Q` to go to the teleporter exit.
* **Spy: Taunt:** Automatically declocks the spy before performing a taunt. Bound to `G`.
* **Spy: Keypad Disguise:** Quickly disguide as a class by pressing `1-9` on the keypad. Pressing the `DELETE` keypad key will switch teams.
* **Spy: Auto Disguise:** Automatically disguises the Spy when clicking `MOUSE1`. If this is not desirable, use `MOUSE3` to perform a normal left-click. Press `R` at any time to disable all auto disguise functions. This script also automatically changes the disguise's current weapon when switching weapons.

## Settings
The config comes with several user editable settings; edit them in `overrides\game_overrides.cfg`:
* `modKey`
* `wait_tester`
* `interp`
* `crouch_jump`
* `toggle_autoreload`
* `netgraph`
* `toggle_viewmodel`
* `toggle_voicechat`
* `toggle_textchat`
* `loadout_switcher`
* `hud_player_model`
* `medic_uber_switch`

For class-specific config settings you can find them in the folder `overrides` and edit them in the class-specific config file e.g. (`overrides\demoman.cfg`):
* `slot`
* `interp`
* `eureka_effect`
* `toggle_scout_secondary`
* `jarate`
* `no_auto_rezoom`
* `rocket_jump`
* `secondary_buff`
* `keypad_disguise`
* `spy_taunt`
* `disguise_weapon`
* `disguise_attack`

## HUD (Recommended)
* [FlawHUD](https://huds.tf/site/s-FlawHUD) a minimalistic designed HUD with dark themed colours.

## Mods (Optional)
* [Disable Incoming Message](https://drive.google.com/file/d/12EYvAGVP4W4OX7dves0kpylp-4v2ioCB/view) removes Miss Pauling's voice lines for quests and the incoming message HUD panel.
* [No Hats Mod](https://github.com/Fedora31/no-hats-bgum/tree/master) removes cosmetics, unusual effects, festiviziers and other things.
* [Old Sticky Jumper and Rocket Jumper Skins](https://gamebanana.com/mods/198851).
* [70 FOV Fix Pack](https://gamebanana.com/mods/198862) **Note:** Doesn't work on Valve servers.
* [Missing Killicons Pack](https://steamcommunity.com/sharedfiles/filedetails/?id=2156604959).
* [Improved and Aligned Medic Heal Beam](https://gamebanana.com/mods/12020).

## To-Do
* Scout: Make `Secondary Weapon Toggle` use the Modkey to switch between modes (mad milk, winger, or off).

## Known Bugs

## Credits
* [mastercomfig](https://mastercomfig.com/).
* [Team Fortress 2 Wiki](http://wiki.teamfortress.com) for their scripting tutorials.
* [Lyrositor](https://github.com/Lyrositor)'s [TF2 Scripts](https://github.com/Lyrositor/TF2-Scripts).
* [clovervidia](https://steamcommunity.com/id/clovervidia) for their [Close Captions in TF2](https://steamcommunity.com/sharedfiles/filedetails/?id=167785751s) guide.
* [Dewgmztv](https://gamebanana.com/members/1432181)'s [Toggle Auto Disguise on attack](https://gamebanana.com/scripts/8925) spy script.