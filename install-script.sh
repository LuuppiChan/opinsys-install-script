#!/usr/bin/env bash

value=0

echo
echo This script needs elevated privileges to run.
echo If you didn\'t run this with sudo it\'ll ask you the password now.
echo

#ask for sudo
[ "$UID" -eq 0 ] || exec sudo bash "$0" "$@"

#I think this has no purpose.
#if [ $EUID != 0 ]; then
#	sudo "$0" "$@"
#	exit $?
#fi

while true; do
	{
while true; do

echo
echo Welcome to the install script
echo
echo 1 install Steam
echo 2 install Minecraft Launcher
echo 3 install Discord
echo 4 install Vesktop
echo 5 install Brave
echo type \"l\" for app launcher
echo type \"u\" for uninstaller
echo type \"q\" to quit
echo

read -p "Value: " value
echo

case $value in
	1|steam|Steam) 
		echo "Installing Steam..."
		wget https://cdn.akamai.steamstatic.com/client/installer/steam.deb
		sudo dpkg -i steam.deb
		rm steam.deb
		echo "Installed" ;;

	2|minecraft|Minecraft)
		echo "Installing Minecraft Launcher..."
		wget https://launcher.mojang.com/download/Minecraft.deb
		sudo dpkg -i Minecraft.deb
		rm Minecraft.deb
		echo "Installed" ;;
	3|discord|Discord)
		echo "Installing Discord..."
		flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
		flatpak install -y flathub com.discordapp.Discord
		echo "Installed" ;;
	4|vesktop|Vesktop)
		echo "Installing Vesktop..."
		flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
		flatpak install -y flathub dev.vencord.Vesktop
		echo "Installed" ;;
	5|brave|Brave)
		echo "Installing Brave..."
		sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
		echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
		sudo apt update
		sudo apt install -y brave-browser
		echo "Installed" ;;
	u|uninstaller|Uninstaller) break;; #uninstaller after while loop
	l|o|launcher|Launcher) break;; #launcher after uninstaller
	q|x|quit|exit) echo "Exitting..." 
		exit ;;
	*) echo "Invalid option, try again" ;;
esac

done

#value to launcher
if [ value=launcher ]; then
	value=l
fi

if [ value=Launcher ]; then
	value=l
fi

if [ value=o ]; then
	value=l
fi


#value to uninstaller
if [ value=uninstaller ]; then
	value=u
fi

if [ value=Uninstaller ]; then
	value=u
fi



#uninstaller
echo

while [ $value=u ]; do

echo
echo Welcome to the uninstaller
echo
echo 1 uninstall Steam
echo 2 uninstall Minecraft Launcher
echo 3 uninstall Discord
echo 4 uninstall Vesktop
echo 5 uninstall Brave
echo \"i\" back to installer menu
echo \"q\" to quit
echo

read -p "Value: " value
echo

case $value in
	1|steam|Steam) 
		echo "Uninstalling Steam..."
		wget https://cdn.akamai.steamstatic.com/client/installer/steam.deb
		sudo dpkg --remove -i steam.deb
		rm steam.deb
		echo "Uninstalled" ;;

	2|minecraft|Minecraft)
		echo "uninstalling Minecraft Launcher..."
		wget https://launcher.mojang.com/download/Minecraft.deb
		sudo dpkg --remove -i Minecraft.deb
		rm Minecraft.deb
		echo "Uninstalled" ;;
	3|discord|Discord)
		echo "Uninstalling Discord..."
		flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
		flatpak uninstall -y flathub com.discordapp.Discord
		echo "Uninstalled" ;;
	4|vesktop|Vesktop)
		echo "Uninstalling Vesktop..."
		flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
		flatpak uninstall -y flathub dev.vencord.Vesktop
		echo "Uninstalled" ;;
	5|brave|Brave)
		echo "Uninstalling Brave..."
		sudo apt remove -y brave-browser
		echo "Uninstalled" ;;
	i|installer|Installer|s)
		break ;;
	q|x|quit|exit) echo "Exitting..." 
		exit ;;
	*) echo "Invalid option, try again" ;;
esac

done



#app launch script

echo

while [ $value=l ]; do

echo
echo Welcome to the app launcher
sleep 1 #sleep 1
echo
echo YOU CAN ALWAYS PRESS THE WINDOWS KEY AND SEARCH THE APP THERE!
sleep 1 #sleep 1
echo Remember to keep the terminal open while the app is running.
sleep 1 #sleep 1
echo
echo 1 launch Steam
echo 2 launch Minecraft Launcher
echo 3 launch Discord
echo 4 launch Vesktop
echo 5 launch Brave
echo \"i\" back to installer menu
echo \"q\" to quit
echo

read -p "Value: " value
echo

case $value in
	1|steam|Steam) 
		echo "Launching Steam..."
		steam
		echo "Exited Steam" ;;

	2|minecraft|Minecraft)
		echo "Launching Minecraft Launcher..."
		minecraft-launcher
		echo "Exited Minecraft Launcher" ;;
	3|discord|Discord)
		echo "Launching Discord..."
		flatpak run com.discordapp.Discord
		echo "Exited Discord" ;;
	4|vesktop|Vesktop)
		echo "Launching Vesktop..."
		flatpak run dev.vencord.Vesktop
		echo "Exited Vesktop" ;;
	5|brave|Brave)
		echo "Launching Brave..."
		sudo apt remove -y brave-browser
		echo "Exited Brave" ;;
	i|installer|Installer|s)
		break ;;
	q|x|quit|exit) echo "Exitting..." 
		exit ;;
	*) echo "Invalid option, try again" ;;
esac

done

value=0

}
done


