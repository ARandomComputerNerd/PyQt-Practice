# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpotD.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import os
from bs4 import BeautifulSoup
import pytube
from pytube import YouTube
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from moviepy.editor import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(800, 600)
        MainWindow.setStyleSheet("background-color: black;")
        MainWindow.setWindowTitle("SpotiDown v0.1 BETA")
        self.ytlink= ""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LinkInput = QtWidgets.QLineEdit(self.centralwidget)
        self.LinkInput.setGeometry(QtCore.QRect(40, 160, 591, 51))
        self.LinkInput.setStyleSheet("QLineEdit\n"
"{\n"
"     color: white;\n"
"     padding: 10px;\n"
"     background-color: rgba(255,255,255,125);\n"
"     border-radius: 25px;\n"
"     \n"
"    font: 63 10pt \"Segoe UI Semibold\";\n"
"}")
        self.LinkInput.setObjectName("LinkInput")
        self.DownloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadButton.setGeometry(QtCore.QRect(640, 160, 131, 51))
        self.DownloadButton.clicked.connect(lambda: self.getYtLinkFromSpotify())
        self.DownloadButton.setStyleSheet("QPushButton\n"
"{\n"
"    color: white;\n"
"    background-color: green;\n"
"    border-radius: 25px;\n"
"    \n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color: black;\n"
"    background-color: lime;\n"
"    border-radius: 25px;\n"
"    \n"
"    font: 75 12pt \"Segoe UI\";\n"
"}")
        self.DownloadButton.setObjectName("DownloadButton")
        self.HeadingLabel = QtWidgets.QLabel(self.centralwidget)
        self.HeadingLabel.setGeometry(QtCore.QRect(240, 50, 361, 41))
        self.HeadingLabel.setStyleSheet("QLabel\n"
"{  \n"
"     color: white;\n"
"     \n"
"    font: 63 20pt \"Segoe UI Semibold\";\n"
"}")
        self.HeadingLabel.setObjectName("HeadingLabel")
        self.LDToggle = QtWidgets.QPushButton(self.centralwidget)
        self.LDToggle.clicked.connect(lambda: self.lightDark())
        self.LDToggle.setGeometry(QtCore.QRect(30, 470, 131, 51))
        self.LDToggle.setStyleSheet("QPushButton\n"
"{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 25px;\n"
"    \n"
"    font: 75 12pt \"Segoe UI\";\n"
"}")
        self.LDToggle.setObjectName("LDToggle")
        self.InfoPanel = QtWidgets.QLabel(self.centralwidget)
        self.InfoPanel.setGeometry(QtCore.QRect(40, 240, 721, 211))
        self.InfoPanel.setStyleSheet("QLabel\n"
"{\n"
"     color: white;\n"
"     \n"
"    font: 63 16pt \"Segoe UI\";\n"
"}")
        self.InfoPanel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.InfoPanel.setObjectName("InfoPanel")
        self.ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ProgressBar.setGeometry(QtCore.QRect(310, 470, 461, 51))
        self.ProgressBar.setStyleSheet("QProgressBar\n"
"{  \n"
"     border-radius: 25px;\n"
"     border: 1px solid grey;\n"
"     \n"
"}\n"
"QProgressBar::chunk\n"
"{ \n"
"     font: 75 12pt \"Segoe UI\";\n"
"     border-radius: 24px;\n"
"     background-color: white;\n"
"     \n"
"}")
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setObjectName("ProgressBar")
        self.AboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.AboutButton.setGeometry(QtCore.QRect(170, 470, 131, 51))
        self.AboutButton.setStyleSheet("QPushButton\n"
"{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 25px;\n"
"    \n"
"    font: 75 12pt \"Segoe UI\";\n"
"}")
        self.AboutButton.setObjectName("AboutButton")
        self.AboutButton.clicked.connect(lambda: self.showAbout())
        self.ProgressBar.raise_()
        self.LinkInput.raise_()
        self.DownloadButton.raise_()
        self.HeadingLabel.raise_()
        self.LDToggle.raise_()
        self.InfoPanel.raise_()
        self.AboutButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def getYtLinkFromSpotify(self):
      try:
        self.InfoPanel.setText("Grabbing the song...")
        spLink= self.LinkInput.text()
        response = requests.get(spLink)  
        soup= BeautifulSoup(response.content, 'html.parser')   
        song_name_element = soup.text[:soup.text.find("- song and lyrics by")]
        song_artist = soup.text[soup.text.find("song and lyrics by ")+19:soup.text.find("| Spotify")]
        self.ProgressBar.setValue(25)
        self.InfoPanel.setText("Song name: "+song_name_element+"\nArtist: "+song_artist+"\nStarting Download...")  
        DEVELOPER_KEY = "AIzaSyBfWusj0FmsXu0v7vPQllg6OS-buvnPwU4"
        YOUTUBE_API_SERVICE_NAME = "youtube"
        YOUTUBE_API_VERSION = "v3"
        query= song_artist+" "+song_name_element
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        search_response = youtube.search().list(q=query, type="video", part="id,snippet", maxResults=1).execute()
        video_id = search_response["items"][0]["id"]["videoId"]
        self.ytlink = f"https://www.youtube.com/watch?v={video_id}"
        print (self.ytlink)
        self.ProgressBar.setValue(50)
        self.startDownload()
      except:
         self.InfoPanel.setText("Invalid URL!")
    def startDownload(self):
     try:
        yt= YouTube(self.ytlink)
        stream= yt.streams.get_audio_only()
        filepath= os.path.join(QtWidgets.QFileDialog.getExistingDirectory(None, "Select where to store the file").replace("/","\\"))
        stream.download(output_path= filepath)
        self.ProgressBar.setValue(75)
        print(filepath)
        filepath= filepath+"\\"+stream.default_filename
        clip= AudioFileClip(filepath)
        self.ProgressBar.setValue(85)
        print(filepath)
        clip.write_audiofile(filepath.replace(".mp4",".mp3"))
        self.ProgressBar.setValue(100)
        self.InfoPanel.setText(self.InfoPanel.text()+"\nDownloaded successfully!")
     except:
        self.InfoPanel.setText("An error occurred! Maybe retry?")
     finally:
        self.InfoPanel.setText(self.InfoPanel.text()+"\nThanks for using our tool!")
    def lightDark(self):
       if self.LDToggle.text()=="Light mode":
          self.LinkInput.setStyleSheet("QLineEdit\n"
"{\n"
"     color: black;\n"
"     padding: 10px;\n"
"     background-color: rgba(0,0,0,125);\n"
"     border-radius: 25px;\n"
"     \n"
"    font: 63 10pt \"Segoe UI Semibold\";\n"
"}")
          self.DownloadButton.setStyleSheet("QPushButton\n"
"{\n"
"    color: black;\n"
"    background-color: green;\n"
"    border-radius: 25px;\n"
"    \n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color: white;\n"
"    background-color: darkgreen;\n"
"    border-radius: 25px;\n"
"    \n"
"    font: 75 12pt \"Segoe UI\";\n"
"}")
          self.HeadingLabel.setStyleSheet("QLabel\n"
"{  \n"
"     color: black;\n"
"     background-color: white;\n"
"    font: 63 20pt \"Segoe UI Semibold\";\n"
"}")
          self.LDToggle.setStyleSheet("QPushButton\n"
"{\n"
"    color: white;\n"
"    background-color: black;\n"
"    border-radius: 25px;\n"
"    \n"
"    font: 75 12pt \"Segoe UI\";\n"
"}")
          self.LDToggle.setText("Dark mode")
          self.InfoPanel.setStyleSheet("QLabel\n"
"{\n"
"     color: black;\n"
"     background-color: white;\n"
"    font: 63 16pt \"Segoe UI\";\n"
"}")
          self.ProgressBar.setStyleSheet("QProgressBar\n"
"{  \n"
"     border-radius: 25px;\n"
"     border: 2px black;\n"
"     background-color: white;\n"
"}\n"
"QProgressBar::chunk\n"
"{ \n"
"     font: 75 12pt \"Segoe UI\";\n"
"     border-radius: 24px;\n"
"     background-color: black;\n"
"     \n"
"}")
          self.AboutButton.setStyleSheet("QPushButton\n"
"{\n"
"    color: white;\n"
"    background-color: black;\n"
"    border-radius: 25px;\n"
"    \n"
"    font: 75 12pt \"Segoe UI\";\n"
"}")
          MainWindow.setStyleSheet("QMainWindow{background-color: white;}")
       else:
          self.LDToggle.setText("Light mode")
          self.LinkInput.setStyleSheet("QLineEdit\n"
"{\n"
"     color: white;\n"
"     padding: 10px;\n"
"     background-color: rgba(255,255,255,125);\n"
"     border-radius: 25px;\n"
"     \n"
"    font: 63 10pt \"Segoe UI Semibold\";\n"
"}")
          self.DownloadButton.setStyleSheet("QPushButton\n"
"{\n"
"    color: white;\n"
"    background-color: green;\n"
"    border-radius: 25px;\n"
"    \n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color: black;\n"
"    background-color: lime;\n"
"    border-radius: 25px;\n"
"    \n"
"    font: 75 12pt \"Segoe UI\";\n"
"}")
          self.HeadingLabel.setStyleSheet("QLabel\n"
"{  \n"
"     color: white;\n"
"     \n"
"    font: 63 20pt \"Segoe UI Semibold\";\n"
"}")
          self.LDToggle.setStyleSheet("QPushButton\n"
"{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 25px;\n"
"    \n"
"    font: 75 12pt \"Segoe UI\";\n"
"}")
          self.InfoPanel.setStyleSheet("QLabel\n"
"{\n"
"     color: white;\n"
"     \n"
"    font: 63 16pt \"Segoe UI\";\n"
"}")
          self.ProgressBar.setStyleSheet("QProgressBar\n"
"{  \n"
"     border-radius: 25px;\n"
"     border: 1px solid grey;\n"
"     background-color: black;\n"
"}\n"
"QProgressBar::chunk\n"
"{ \n"
"     font: 75 12pt \"Segoe UI\";\n"
"     border-radius: 24px;\n"
"     background-color: white;\n"
"     \n"
"}")
          self.AboutButton.setStyleSheet("QPushButton\n"
"{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 25px;\n"
"    \n"
"    font: 75 12pt \"Segoe UI\";\n"
"}")
          MainWindow.setStyleSheet("QMainWindow{background-color: black}")
    def showAbout(self):
          messagebox= QtWidgets.QMessageBox(icon= QtWidgets.QMessageBox.Information, text= "SpotiDown - A clean Spotify Downloader, handcrafted by a group of passionate engineers.\nRuns on the solid Qt Framework\nDeveloper: S.Haris\nTeamX Corporation\nCopyright 2023-24")
          messagebox.setWindowTitle("About SpotiDown")
          messagebox.exec_()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("SpotiDown v0.1 BETA")
        self.LinkInput.setPlaceholderText(_translate("MainWindow", "Enter the Spotify URI of the song"))
        self.DownloadButton.setText(_translate("MainWindow", "Download"))
        self.HeadingLabel.setText(_translate("MainWindow", "SpotiDown by TeamX"))
        self.LDToggle.setText(_translate("MainWindow", "Light mode"))
        self.InfoPanel.setText(_translate("MainWindow", "No song loaded! Enter the URI and press Download."))
        self.AboutButton.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())