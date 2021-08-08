# ANSI Escape codes:
red='\033[1;31m'
green='\033[1;36m'
reset='\033[0m'

# * Check for all flag
allFlag="false"
while getopts ":a" flag; do
	case ${flag} in
		a)
			allFlag="true"
			;;
		\?)
			echo -e "${red}$0${reset}: The option -${OPTARG} is invalid." >&2
			exit 1
			;;
	esac
done

if [[ $allFlag != "true" && $# == "0" ]]; then
	
	# * Print help
	cat <<EOF
How to use:

	./makelinks.sh [-a | TARGETS...]

Where TARGETS are the names of the packages to link (separated by spaces).
-a: Select all targets.

Examples:

	./makelinks.sh bash
	./makelinks.sh qtile redshift
	./makelinks.sh -a

EOF

elif [[ $allFlag != "true" ]]; then

	# * Iterate over arguments received and link the ones found
	for i in $@; do

		# # BASH
		if [[ $i == "bash" ]]; then
			[ -f "$HOME/.bashrc" ] && rm "$HOME/.bashrc"
			[ -f "$HOME/.bash_aliases" ] && rm "$HOME/.bash_aliases"
			[ -f "$HOME/.bash_variables" ] && rm "$HOME/.bash_variables"
			stow -t "$HOME" bash/
			echo -e "${green}Bash linked successfully!${reset}"

		# # COMPTON
		elif [[ $i == "compton" ]]; then
			[ -d "$HOME/.config/compton" ] && rm -rf "$HOME/.config/compton"
			stow -t "$HOME/.config" compton/
			echo -e "${green}Compton linked successfully!${reset}"

		# # CRONTAB
		elif [[ $i == "crontab" ]]; then
			crontab < crontab/crontab.txt
			echo -e "${green}Crontab linked successfully!${reset}"

		# # GIT
		elif [[ $i == "git" ]]; then
			[ -f "$HOME/.gitconfig" ] && rm "$HOME/.gitconfig"
			stow -t "$HOME" git/
			echo -e "${green}Git linked successfully!${reset}"

		# # NEOFETCH
		elif [[ $i == "neofetch" ]]; then
			[ -d "$HOME/.config/neofetch" ] && rm -rf "$HOME/.config/neofetch"
			stow -t "$HOME/.config" neofetch/
			echo -e "${green}Neofetch linked successfully!${reset}"

		# # QTILE
		elif [[ $i == "qtile" ]]; then
			[ -d "$HOME/.config/qtile" ] && rm -rf "$HOME/.config/qtile"
			stow -t "$HOME/.config" qtile/
			echo -e "${green}Qtile linked successfully!${reset}"

		# # REDSHIFT
		elif [[ $i == "redshift" ]]; then
			[ -f "$HOME/.config/redshift.conf" ] && rm "$HOME/.config/redshift.conf"
			stow -t "$HOME/.config" redshift/
			echo -e "${green}Redshift linked successfully!${reset}"
		
		# ? Not Found
		else
			echo -e "${red}$i not found!${reset}" >&2
		fi
	done

else

	# * Link all

	# # BASH
		[ -f "$HOME/.bashrc" ] && rm "$HOME/.bashrc"
		[ -f "$HOME/.bash_aliases" ] && rm "$HOME/.bash_aliases"
		stow -t "$HOME" bash/
		echo -e "${green}Bash linked successfully!${reset}"

	# # COMPTON
		[ -d "$HOME/.config/compton" ] && rm -rf "$HOME/.config/compton"
		stow -t "$HOME/.config" compton/
		echo -e "${green}Compton linked successfully!${reset}"

	# # CRONTAB
		crontab < crontab/crontab.txt
		echo -e "${green}Crontab linked successfully!${reset}"

	# # GIT
		[ -f "$HOME/.gitconfig" ] && rm "$HOME/.gitconfig"
		stow -t "$HOME" git/
		echo -e "${green}Git linked successfully!${reset}"

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
fi

exit 0;