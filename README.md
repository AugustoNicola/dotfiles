# AugustoNicola/dotfiles
## My personal linux dotfiles // Mis archivos de configuración personales

![Screenshot](https://raw.githubusercontent.com/AugustoNicola/dotfiles/main/screenshot.png?token=ALORPBRCJKKEADUDLEHP5D3AKUENE)

## Packages // Paquetes
* [Bash](https://github.com/AugustoNicola/dotfiles/tree/main/bash)
* [Compton](https://github.com/AugustoNicola/dotfiles/tree/main/compton/compton)
* [Neofetch](https://github.com/AugustoNicola/dotfiles/tree/main/neofetch/neofetch)
* [Qtile](https://github.com/AugustoNicola/dotfiles/tree/main/qtile/qtile)

## English

These are the configuration files from the software that I use regularly: that includes my window manager, text editors, shell and some more, ~~mostly~~ documented with comments in english. **Feel free to read, copy or fork the code that you need!**

For managing the files, I use a small script that uses [GNU stow](https://www.gnu.org/software/stow/) to create symlinks to whenever the config files are expected, while actually residing in the same `~/dotfiles` directory, which makes it really easy to manage. For more information on how to use GNU stow for dotfiles check out [this awesome video by Tech Pills](https://www.youtube.com/watch?v=GqL6W-ua7uQ)

### Usage
In order to use my dotfiles, first clone the repo wherever you want to keep your dotfiles in your machine, and then move to that directory.

#### Using a particular package
In most cases you will only want to use a few of my dotfiles, and not all. Since _(in its current state)_ the `makelinks` script can only copy every single config file at once, you will have to use the `stow` command directly.

1. Delete (or backup somewhere else) the folder or file (depending on the software) responsible for the configuration: 

	**For directories (such as with Qtile):** `rm -rf directory/with/configs`
	
	**For single files (such as .bashrc):** `rm directory/to/file`
	
2. Use the `stow` command:

		stow -t {target_directory} {package/}
		
	Where `target_directory` is the directory in which the config file or directory is required (usually `"$HOME"/.config`) and `package` is the name of the directory in the repo that contains my dotfiles.

#### Using all packages
In case you would want to use all of my dotfiles, you can use the `makelinks` script that I created for myself, by simply:

**WARNING: THIS _WILL_ OVERRIDE YOUR CONFIGURATION FILES FOR EVERY SINGLE PACKAGE CONTAINED WITHIN THE SCRIPT**

	./makelinks


###  Contributing
Contributing in any way (such as proposing different configurations, upgrading the documentation or suggesting better ways of handling the files) are always welcome, and will be thoroughly appreciated!



## Español
Estos son los archivos de configuración que uso: mi gestor de ventanas, editor de texto, shell y algunos más, ~~en su mayoría~~ con comentarios en inglés. **¡Podés leer, usar o modificar el código que necesites!**

Para administrar los archivos, uso un script que con la ayuda de [GNU stow](https://www.gnu.org/software/stow/) crea enlaces simbólicos hacia donde sean necesarios los archivos, mientras que en realidad están en un mismo directorio `~/dotfiles`, por lo que es muy fácil de manejar. Para más información acerca de cómo usar GNU stow para manejar archivos de configuración está [este video del youtuber Tech Pills](https://www.youtube.com/watch?v=GqL6W-ua7uQ)

### Cómo Usar
Para poder usar mis archivos, primero tenés que copiar el repositorio donde quieras guardar las configuraciónes y moverte al directorio.

#### Para un o unos paquetes particulares
Lo más probable es que solo quieras usar uno o algunos de los archuvos, no todos. Como _(por el momento)_ el script `makelinks` solo tiene la capacidad de copiar todos los archivos, vas a tener que usar el comando `stow` directamente.

1. Borrá (o mové a algún otro lugar seguro) el directorio o archivo (dependiendo del paquete) responsable de la configuración: 

	**Para directorios (como Qtile):** `rm -rf directorio/con/configuraciones`
	
	**Para archivos (como el .bashrc de bash):** `rm directorio/al/archivo`
	
2. Usá el comando `stow`:

		stow -t {directorio_objetivo} {paquete/}
		
	Siendo `directorio_objetivo` el directorio donde se requiere el archivo o directorio de configuración (normalmente `"$HOME"/.config`) y `paquete` el nombre del directorio dentro de mi repositorio que contiene el paquete que querés.

#### Para todos los paquetes
Si querés usar todos mis archivos de configuración, podés hacerlo usando el script `makelinks` que hice para mí mismo, corriendo:

**CUIDADO: ESTO VA A BORRAR TUS ARCHIVOS DE CONFIGURACIÓN PREVIOS DE _TODOS_ LOS PAQUETES DENTRO DE MI REPOSITORIO**

	./makelinks

###  Contribuciones
Contribuir de cualquier manera (como puede ser proponer nuevas configuraciones, mejorar la documentación del código, o sugerir mejoras en el manejo de archivos) son siempre bienvenidas, y serán agradecidas!