#!/bin/bash
#* output coloring variables
reset=$( tput sgr 0 );
red=$( tput setaf 1 );
green=$( tput setaf 2 );

# * Check for flags
allFlag="false"
listFlag="false"
while getopts ":al" flag; do
	case ${flag} in
		a)
			allFlag="true"
			;;
		l)
			listFlag="true"
			;;
		\?)
			echo -e "${red}$0${reset}: The option -${OPTARG} is invalid." >&2
			exit 1
			;;
	esac
done

if [[ $allFlag == "true" ]]; then
	# * Link all
	
	# # ALACRITTY
	[ -d "$HOME/.config/alacritty" ] && rm -rf "$HOME/.config/alacritty"
	stow -t "$HOME/.config" alacritty/
	echo -e "${green}Alacritty linked successfully!${reset}"
	
	# # BASH
	[ -f "$HOME/.bashrc" ] && rm "$HOME/.bashrc"
	[ -f "$HOME/.bash_aliases" ] && rm "$HOME/.bash_aliases"
	[ -f "$HOME/.bash_logout" ] && rm "$HOME/.bash_logout"
	stow -t "$HOME" bash/
	echo -e "${green}Bash linked successfully!${reset}"
	
	# # COMPTON
	[ -d "$HOME/.config/compton" ] && rm -rf "$HOME/.config/compton"
	stow -t "$HOME/.config" compton/
	echo -e "${green}Compton linked successfully!${reset}"
	
	# # CRONTAB
	crontab < crontab/crontab.txt
	echo -e "${green}Crontab linked successfully!${reset}"
	
	# # SCRIPTS
	[ -d "$HOME/Scripts" ] && rm -rf "$HOME/Scripts"
	stow -t "$HOME" scripts/ 
	echo -e "${green}Scripts linked successfully!${reset}"
	
	# # NEOFETCH
	[ -d "$HOME/.config/neofetch" ] && rm -rf "$HOME/.config/neofetch"
	stow -t "$HOME/.config" neofetch/
	echo -e "${green}Neofetch linked successfully!${reset}"
	
	# # QTILE
	[ -d "$HOME/.config/qtile" ] && rm -rf "$HOME/.config/qtile"
	stow -t "$HOME/.config" qtile/
	echo -e "${green}Qtile linked successfully!${reset}"
	
	# # REDSHIFT
	[ -f "$HOME/.config/redshift.conf" ] && rm "$HOME/.config/redshift.conf"
	stow -t "$HOME/.config" redshift/
	echo -e "${green}Redshift linked successfully!${reset}"
	
	# # ROFI
	[ -d "$HOME/.config/rofi" ] && rm -rf "$HOME/.config/rofi"
	stow -t "$HOME/.config" rofi/
	echo -e "${green}Rofi linked successfully!${reset}"
	
	# # VIS
	[ -d "$HOME/.config/vis" ] && rm -rf "$HOME/.config/vis"
	stow -t "$HOME/.config" vis/
	echo -e "${green}Vis linked successfully!${reset}"
	
	# # VSCODE
	[ -f "$HOME/.config/Code/User/settings.json" ] && rm "$HOME/.config/Code/User/settings.json"
	[ -f "$HOME/.config/Code/User/keybindings.json" ] && rm "$HOME/.config/Code/User/keybindings.json"
	[ -f "$HOME/.config/Code/User/.prettierrc" ] && rm "$HOME/.config/Code/User/.prettierrc"
	[ -f "$HOME/.config/Code/User/cheatsheet.txt" ] && rm "$HOME/.config/Code/User/cheatsheet.txt"
	stow -t "$HOME/.config/Code/User" vscode/
	echo -e "${green}VSCode linked successfully!${reset}"
	
	# # ZATHURA
	[ -d "$HOME/.config/zathura" ] && rm -rf "$HOME/.config/zathura"
	stow -t "$HOME/.config" zathura/
	echo -e "${green}Zathura linked successfully!${reset}"
	
	# # ZSH
	[ -d "$HOME/.config/zsh" ] && rm -rf "$HOME/.config/zsh"
	stow -t "$HOME/.config" zsh/
	echo -e "${green}Zsh linked successfully!${reset}"

elif [[ $listFlag == "true" ]]; then
	# * List all possible targets
	
	cat <<EOF
Possible targets:

	alacritty
	bash
	compton
	crontab
	scripts
	neofetch
	qtile
	redshift
	rofi
	vis
	vscode
	zathura
	zsh

EOF

elif [[ ! $# == "0" ]]; then
	# * Iterate over arguments received and link the ones found
	
	for i in $@; do
		
		case $i in
			
			"alacritty")
				[ -d "$HOME/.config/alacritty" ] && rm -rf "$HOME/.config/alacritty"
				stow -t "$HOME/.config" alacritty/
				echo -e "${green}Alacritty linked successfully!${reset}"
				;;
			
			"bash")
				[ -f "$HOME/.bashrc" ] && rm "$HOME/.bashrc"
				[ -f "$HOME/.bash_aliases" ] && rm "$HOME/.bash_aliases"
				[ -f "$HOME/.bash_variables" ] && rm "$HOME/.bash_variables"
				stow -t "$HOME" bash/
				echo -e "${green}Bash linked successfully!${reset}"
				;;
			
			"compton")
				[ -d "$HOME/.config/compton" ] && rm -rf "$HOME/.config/compton"
				stow -t "$HOME/.config" compton/
				echo -e "${green}Compton linked successfully!${reset}"
				;;
			
			"crontab")
				crontab < crontab/crontab.txt
				echo -e "${green}Crontab linked successfully!${reset}"
				;;
			
			"scripts")
				[ -d "$HOME/Scripts" ] && rm -rf "$HOME/Scripts"
				stow -t "$HOME" scripts/ 
				echo -e "${green}Scripts linked successfully!${reset}"
				;;
			
			"neofetch")
				[ -d "$HOME/.config/neofetch" ] && rm -rf "$HOME/.config/neofetch"
				stow -t "$HOME/.config" neofetch/
				echo -e "${green}Neofetch linked successfully!${reset}"
				;;
			
			"qtile")
				[ -d "$HOME/.config/qtile" ] && rm -rf "$HOME/.config/qtile"
				stow -t "$HOME/.config" qtile/
				echo -e "${green}Qtile linked successfully!${reset}"
				;;
			
			"redshift")
				[ -f "$HOME/.config/redshift.conf" ] && rm "$HOME/.config/redshift.conf"
				stow -t "$HOME/.config" redshift/
				echo -e "${green}Redshift linked successfully!${reset}"
				;;
			
			"rofi")
				[ -d "$HOME/.config/rofi" ] && rm -rf "$HOME/.config/rofi"
				stow -t "$HOME/.config" rofi/
				echo -e "${green}Rofi linked successfully!${reset}"
				;;
			
			"vis")
				[ -d "$HOME/.config/vis" ] && rm -rf "$HOME/.config/vis"
				stow -t "$HOME/.config" vis/
				echo -e "${green}Vis linked successfully!${reset}"
				;;
			
			"vscode")
				[ -f "$HOME/.config/Code/User/settings.json" ] && rm "$HOME/.config/Code/User/settings.json"
				[ -f "$HOME/.config/Code/User/keybindings.json" ] && rm "$HOME/.config/Code/User/keybindings.json"
				[ -f "$HOME/.config/Code/User/.prettierrc" ] && rm "$HOME/.config/Code/User/.prettierrc"
				[ -f "$HOME/.config/Code/User/cheatsheet.txt" ] && rm "$HOME/.config/Code/User/cheatsheet.txt"
				stow -t "$HOME/.config/Code/User" vscode/
				echo -e "${green}VSCode linked successfully!${reset}"
				;;
			
			"zathura")
				[ -d "$HOME/.config/zathura" ] && rm -rf "$HOME/.config/zathura"
				stow -t "$HOME/.config" zathura/
				echo -e "${green}Zathura linked successfully!${reset}"
				;;
			
			"zsh")
				[ -d "$HOME/.config/zsh" ] && rm -rf "$HOME/.config/zsh"
				stow -t "$HOME/.config" zsh/
				echo -e "${green}Zsh linked successfully!${reset}"
				;;
			
			# ? Not Found
			*)
				echo -e "${red}$i not found!${reset}" >&2
				;;
		esac
	done

else
	# * Print help
	
	cat <<EOF
How to use:

	./makelinks.sh [-a | -l | TARGETS...]

Where TARGETS are the names of the packages to link (separated by spaces).
-a: Select all targets.
-l: List all possible targets.

Examples:

	./makelinks.sh bash
	./makelinks.sh qtile redshift
	./makelinks.sh -a
	./makelinks.sh -l

EOF

fi

exit 0;