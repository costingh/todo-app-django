

/* #############################################################################################################
######################################### Make scrollbar transparent on scroll #########################################
################################################################################################################ */

window.addEventListener('scroll', this.handleScroll, true);

handleScroll = (e) => {
    if (e.target.classList.contains("on-scrollbar") === false) {
        e.target.classList.add("on-scrollbar");
    } 
}


/* #############################################################################################################
######################################### Dark / Light theme selection #########################################
################################################################################################################ */

class ChangeColorMode {
    constructor (toggler, currentTheme) {
        this.toggler = document.querySelector(toggler);
        this.currentTheme = localStorage.getItem(currentTheme);
    }

    changeMode () {
        this.toggler.addEventListener('change', (event) => {
            if(event.target.checked) {
                document.documentElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
            } else {
                document.documentElement.setAttribute('data-theme', 'light');
                localStorage.setItem('theme', 'light');
            }
        }, false);
    }

    readAndSet () {
        if (this.currentTheme) {
            document.documentElement.setAttribute('data-theme', this.currentTheme);
          
            if (this.currentTheme === 'dark') {
                this.toggler.checked = true;
            }
        }

        this.changeMode();
    }
}

let colorMode = new ChangeColorMode('#checkbox', 'theme');
colorMode.readAndSet();
