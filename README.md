# Security Toolbox als Webdienst in der Cloud

> Abschlussprojekt von Stevan Medic – ZLI 2025  
> Sicherheits-Tools, gehostet auf eigenem Cloudserver mit Weboberfläche

---

## Projektbeschreibung

Dieses Projekt stellt eine **Security Toolbox** als **Webdienst** zur Verfügung. Es handelt sich um eine lokal gehostete Webseite, die nützliche Sicherheitstools wie Passwortgenerator, IP-Check, HTTP-Header-Scanner und mehr anbietet. Die Oberfläche ist in HTML/CSS gestaltet, die Tools basieren auf JavaScript oder Python (Flask). Der Webserver läuft auf einem Ubuntu-Server in einer VM (lokal via VMware oder Proxmox).

---

## Features

| Tool                  | Beschreibung                                                                 |
|-----------------------|------------------------------------------------------------------------------|
| Passwortgenerator  | Zufällige sichere Passwörter, generiert lokal im Browser                     |
| IP-Check Tool       | Zeigt die öffentliche IP + Geo-Daten via API (clientseitig)                  |
| HTTP-Header-Scanner | Flask-Backend analysiert HTTP-Header einer angegebenen URL                   |
| Passwort-Checker    | Bewertet Passwortstärke nach Länge, Zeichenarten etc.                        |
| Hash-Generator      | SHA-256, SHA-512 oder MD5 Hashes erzeugen, ohne Serververbindung             |
| Größen-Konverter    | Bytes in KB/MB/GB umrechnen mit einfacher JS-Logik                           |
| Hexadezimal-Konverter | Wandelt Hex-Werte in Dezimalzahlen um                                       |

---

## Technische Umsetzung

- **Backend:** Python (Flask), systemd-Dienste
- **Frontend:** HTML, CSS, JavaScript
- **Webserver:** Apache2 auf Ubuntu 24.04 LTS
- **Zertifikate:** Selbstsigniertes SSL (Let's Encrypt fehlgeschlagen)
- **Hosting:** VM über Proxmox oder VMware Workstation

---

## 📁 Projektstruktur

```plaintext
/var/www/html/           → Startseite & HTML-Tools
/opt/tools/              → Python-Backends mit Flask
/etc/apache2/            → Apache-Konfigurationen
/etc/systemd/system/     → Eigene systemd-Dienste für Flask-Apps
/backups/                → Lokale Backups (automatisiert via Cron)
![image](https://github.com/user-attachments/assets/d9b2029e-afd1-41fa-88a9-79ce28cca580)

```




---

## Backup-Konzept(Erweiterung)

- Tägliche inkrementelle Backups (`rsync`)
- Wöchentliche Vollbackups (`tar.gz`)
- Speicherung lokal & optional extern (Cloud/USB)
- Wiederherstellung einfach über Kopie oder `tar -xzf`
- Automatisiert mit `cron`, gesichert mit `chmod`, optional GPG-Verschlüsselung

---

## Bekannte Probleme

- Zugriff von aussen gescheitert (Portweiterleitung, Firewall)
- Let's Encrypt-Zertifikat konnte nicht ausgestellt werden
- Nested Virtualization unter VMware erschwerte KVM-Nutzung von Proxmox
- Übergang zu eigenständiger Ubuntu-VM war notwendig

---

## Arbeitsjournal

Alle Projekttage wurden dokumentiert: Einrichtung, Probleme, Lösungen, Fortschritte.  
→ Siehe Abschnitt **Arbeitsjournal** in der Abschlussdokumentation.

---

## ToDo (optional)

- [ ] Öffentlichen Zugriff (HTTP/HTTPS) ermöglichen  
- [ ] Domain mit Freenom verknüpfen  
- [ ] HTTPS mit Let's Encrypt aktivieren  
- [ ] Weitere Tools ergänzen (z. B. Portscanner, Hashvergleich etc.)

---

## Autor

**Stevan Medic**  
Projekt im Rahmen des ZLI-Basislehrjahrs  
Firma: Bison Schweiz AG – Winterthur

---

## Links

- [GitHub Repository]([https://github.com/dein-repo-link-hier](https://github.com/Stevo-08/Abschlussprojekt_2025_PLA-2_stemed_Board_Security-Toolbox-als-Webdienst-in-der-Cloud))
- [Abschlussdokumentation (PDF)](./Abschlussdokumentation_2025_PLA-2_stemed.docx)


---

## Lizenz

Dieses Projekt dient zu Ausbildungszwecken im Bereich IT-Security & Webentwicklung.  
Kein Produktivbetrieb – Nutzung auf eigene Verantwortung.
