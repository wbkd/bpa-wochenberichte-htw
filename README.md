# Hi!

Willkommen zum Semesterprojekt von [FragDenStaat](https://fragdenstaat.de/) und [webkid](https://webkid.io/)! Ihr erreicht uns am besten über den Slack-Channel (semesterprojekthtw.slack.com). Für alle inhaltlichen Dinge ist Arne der Ansprechpartner, für alle technischen Fragen Christopher. Wir freuen uns, dass ihr dabei seid!

## Zusammenfassung

Kein Kanzler vor Angela Merkel hat seine Politik so stark an Umfragen ausgerichtet wie sie. Im Semesterprojekt werten wir hunderte Umfrageberichte-PDFs der letzten Jahre aus, die das Bundespresseamt jede Woche Angela Merkel vorlegt. Wir haben sie per Informationsfreiheitsgesetz vom Kanzleramt erhalten. Mit den Daten aus den Dokumenten zeichnen wir Merkels Kanzlerschaft nach: Welche Themen standen in den Umfragen im Mittelpunkt, wann richtete sie sich an ihnen aus? Welche Informationen lagen dem Kanzleramt vor wichtigen Entscheidungen vor - und welche Themen hatte sie nicht im Blick?

## Datensatz

Der Datensatz umfasst rund 200 PDF-Dokumente (je ein Bericht pro Woche, seit Mitte 2015). In den Dokumenten sind Daten in unterschiedlichen Formaten enthalten (Text, Tabellen, Diagramme, ...). Diese Daten wollen wir aus den PDFs "befreien", säubern und in ein maschinenlesbares Format bringen, damit wir die Möglichkeit haben, die Daten der Berichte zu vergleichen und auszuwerten.

Für Datenjournalist*innen sind PDF-Dokumente als Datenquelle oft problematisch, weil sich Informationen aus PDFs nur schwer extrahieren lassen. Selbst eine Tabelle aus einem PDF-Dokument in Excel zu kopieren ist oft nicht möglich. Dafür gibt es Tools wie [Tabula](https://tabula.technology/), die allerdings auch händisch bedient werden müssen. Bei einer großen Anzahl an Dokumenten ist dies sehr mühsam. Daher wollen wir eine Möglichkeit finden, die PDFs automatisiert einzulesen und die Daten in ein besser lesbares Format zu extrahieren, zum Beispiel JSON oder CSV.

## Beispielprojekte

- [Darüber spricht der Bundestag](https://www.zeit.de/politik/deutschland/2019-09/bundestag-jubilaeum-70-jahre-parlament-reden-woerter-sprache-wandel#s=sozialismus%2Cuniversit%C3%A4ten), Zeit Online: Interaktive Auswertung aller Wörter, die seit 1949 im Bundestag gesprochen wurden. Dazu wurden alle [Plenarprotokolle](https://www.bundestag.de/services/opendata) eingelesen, bereinigt und durchsuchbar gemacht. Ähnlich: [How the Internet* talks](https://projects.fivethirtyeight.com/reddit-ngram) von FiveThirtyEight.
- [Grippe Monitor](https://interaktiv.morgenpost.de/grippe-monitor-deutschland/), Berliner Morgenpost: Übersicht aller Grippe-Fälle in Deutschland. Die Daten werden vom RKI als [PDF-Wochenberichte veröffentlicht](https://influenza.rki.de/Wochenberichte.aspx). Um diese visualisieren zu können musste ebenfalls ein Script programmiert werden, das die Daten aus den PDFs befreit.

## Vorbereitung


### Tools

1. [Github](https://github.com/)-Account: Wir werden Github verwenden, um gemeinsam an Code zu arbeiten. Falls ihr noch keinen Account habt, erstellt euch bitte einen und schickt euren Username an Christopher im Slack.
2. [Git](https://git-scm.com): Um am Code kollaborativ zu arbeiten, benötigen wir das Command-Line-Tool "git". Wahrscheinlich ist es bei euch schon installiert. Das könnt ihr checken, indem ihr im Terminal `git --version` eingebt. Falls es noch nicht installiert ist könnt ihr es [hier](https://git-scm.com/downloads) runterladen.
3. Pyhton installieren, zB. anhand von [pyenv](https://github.com/pyenv/pyenv) 
4. [Anaconda](https://www.anaconda.com/products/individual) ist ein Toolkit für Datenanalyse. Das Toolkit enthält diverse Programme um mit Daten zu arbeiten. Unter anderem ist [Jupyter](https://jupyter.org/) enthalten. Anaconda könnt ihr [hier](https://www.anaconda.com/products/individual) runterladen und installieren.
    **oder alternativ:**
    1. Virtuelle Umgebung aufsetzen anhand von [venv](https://docs.python.org/3/library/venv.html)
    2. Für das Projekt benötigte Pakete liegen in einer requirements.txt Datei und werden installiert über `pip install -r requirements.txt`
4. [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) ist eine interaktive Entwicklungsumgebung für Datenanalyse, die wir nutzen wollen um gemeinsam die Daten aufzubereiten und zu visualisieren. Bei Nutzung von Anaconda könnt ihr Jupyter Lab über diesen Befehl im Terminal installieren: `conda install -c conda-forge jupyterlab`. In eurer virtuellen Ungebung installiert ihr es wie unter Punkt 4.2 beschrieben.

### Hello World

(0. Einen bestehenden oder neuen SSH-Key bei Github hinterlegen, damit beim pull/push nicht immer das Passwort eingegeben werden muss. [Anleitung](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh))
1. Repository clonen: `git clone git@github.com:wbkd/bpa-wochenberichte.git`
2. In den Ordner wechseln: `cd bpa-wochenberichte`
3. Jupyter Lab starten: `jupyter lab`
4. Neues Notebook unter `/notebooks/[DeinName].ipynb` erstellen
5. Zu Git hinzufügen: `git add ./notebooks/[DeinName].ipynb`
6. Git Commit erstellen: `git commit -m "hello world"`
7. Zu Github pushen: `git push origin main`

### Bibliotheken

#### Datenaufbereitung

* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/)

#### Datenvisualisierung

* [matplotlib](https://matplotlib.org/)
* [plotly](https://plotly.com/python/ipython-notebook-tutorial/)

## Repo Struktur

* `/rawdata` enthält die PDF-Wochenberichte
* `/notebooks` enthält unsere Jupyter Notebooks

## Für später

- JS Kernel (https://github.com/n-riesco/ijavascript)
- Visualisierungen
- Tabellen-Output

## Arbeiten mit den finalen Python-Skripten

Es gibt eine requirements-Datei, die alle notwendigen Module enthält. Diese kann mit dem Befehl `pip install -r requirements.txt` installiert werden.
Wenn ihr Anaconda bereits installiert habt, funktionieren alle Module. Ansonsten braucht ihr noch ghostscript -> `$ brew install ghostscript tcl-tk`, damit das Modul camelot funktioniert.
