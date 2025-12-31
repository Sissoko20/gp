from xhtml2pdf import pisa
from datetime import datetime

def generate_pdf(html_content, filename="facture.pdf"):
    with open(filename, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)
    return filename if not pisa_status.err else None

def build_facture_html(data, type_doc="Reçu"):
    logo_path = "assets/logo.png"
    signature_path = "assets/signature.png"
    today = datetime.today().strftime("%d/%m/%Y")

    footer_text = """
    <hr>
    <div style="font-size:11px; text-align:center; margin-top:20px;">
    MABOU-INSTRUMED-SARL | RCCM : Ma.Bko.2023.M11004 | NIF : 084148985H | Lassa  
    Tél : +223 74 56 43 95 | Banque d'Afrique | Email : sidibeyakouba@gmail.com
    </div>
    """

    html = f"""
    <div style="font-family:Arial; font-size:13px; padding:10px; width:650px; line-height:1.3;">

        <!-- En-tête -->
        <div style="display:flex; justify-content:space-between;">
            <div>
                <img src="{logo_path}" width="70"><br>
                <b>MABOU-INSTRUMED-SARL</b><br>
                Lassa<br>
                Tél : +223 74 56 43 95<br>
                Banque d'Afrique<br>
                Email : sidibeyakouba@gmail.com
            </div>
            <div style="text-align:right;">
                <b>Client :</b> {data['client_name']}<br>
                Tél : {data.get('client_phone', '')}<br>
                Email : {data.get('client_email', '')}
            </div>
        </div>

        <hr>

        <h3 style="text-align:center; margin:10px 0;">REÇU DE PAIEMENT</h3>

        <p style="margin:4px 0;"><b>Objet :</b> {data['objet']}</p>
        <p style="margin:4px 0;"><b>Montant payé :</b> {data['amount']:.2f} FCFA</p>

        <hr>

        <!-- Signature + Date -->
        <div style="display:flex; justify-content:flex-end; align-items:center; gap:10px; margin-top:20px;">
            <p style="margin:0;">Fait à Bamako, le {today}</p>
            <img src="{signature_path}" width="220">
        </div>

        {footer_text}
    </div>
    """
    return html



def build_facture_html(data, type_doc="Facture"):
    logo_path = "assets/logo.png"
    signature_path = "assets/signature.png"
    today = datetime.today().strftime("%d/%m/%Y")

    footer_text = """
    <hr>
    <div style="font-size:11px; text-align:center; margin-top:20px;">
    MABOU-INSTRUMED-SARL | RCCM : Ma.Bko.2023.M11004 | NIF : 084148985H | Lassa  
    Tél : +223 74 56 43 95 | Banque d'Afrique | Email : sidibeyakouba@gmail.com
    </div>
    """

    # ---------------- FACTURE ----------------
    if type_doc == "Facture":
        items_html = ""
        total_ht = 0
        for item in data["items"]:
            montant = item["qty"] * item["price"]
            total_ht += montant
            tva = item.get("tva", 0)
            items_html += f"""
            <tr>
                <td style="padding:4px;">{item['description']}</td>
                <td style="text-align:center;">{item['date']}</td>
                <td style="text-align:center;">{item['qty']}</td>
                <td style="text-align:right;">{item['price']:.2f} FCFA</td>
                <td style="text-align:center;">{tva}%</td>
                <td style="text-align:right;">{montant:.2f} FCFA</td>
            </tr>
            """

        tva_total = total_ht * 0.18
        total_ttc = total_ht + tva_total

        html = f"""
        <div style="font-family:Arial; font-size:13px; padding:10px; width:650px; line-height:1.3;">
            <!-- En-tête -->
            <div style="display:flex; justify-content:space-between;">
                <div>
                    <img src="{logo_path}" width="70"><br>
                    <b>MABOU-INSTRUMED-SARL</b><br>
                    Lassa<br>
                    Tél : +223 74 56 43 95<br>
                    Banque d'Afrique<br>
                    Email : sidibeyakouba@gmail.com
                </div>
                <div style="text-align:right;">
                    <b>Client :</b> {data['client_name']}<br>
                    Tél : {data['client_phone']}<br>
                    Email : {data['client_email']}
                </div>
            </div>

            <hr>
            <h3 style="text-align:center; margin:10px 0;">FACTURE</h3>

            <table style="width:100%; border-collapse:collapse; font-size:13px;" border="1">
                <thead>
                    <tr>
                        <th>Description</th><th>Date</th><th>Qté</th><th>Prix unitaire</th><th>TVA</th><th>Montant</th>
                    </tr>
                </thead>
                <tbody>
                    {items_html}
                </tbody>
            </table>

            <p><b>Total HT :</b> {total_ht:.2f} FCFA</p>
            <p><b>TVA 18% :</b> {tva_total:.2f} FCFA</p>
            <p><b>Total TTC :</b> {total_ttc:.2f} FCFA</p>

            <hr>
            <div style="display:flex; justify-content:flex-end; align-items:center; gap:10px; margin-top:20px;">
                <p style="margin:0;">Fait à Bamako, le {today}</p>
                <img src="{signature_path}" width="220">
            </div>

            {footer_text}
        </div>
        """
        return html

    # ---------------- REÇU ----------------
    elif type_doc == "Reçu":
        html = f"""
        <div style="font-family:Arial; font-size:13px; padding:10px; width:650px; line-height:1.3;">
            <!-- En-tête -->
            <div style="display:flex; justify-content:space-between;">
                <div>
                    <img src="{logo_path}" width="70"><br>
                    <b>MABOU-INSTRUMED-SARL</b><br>
                    Lassa<br>
                    Tél : +223 74 56 43 95<br>
                    Banque d'Afrique<br>
                    Email : sidibeyakouba@gmail.com
                </div>
                <div style="text-align:right;">
                    <b>Client :</b> {data['client_name']}<br>
                    Tél : {data.get('client_phone', '')}<br>
                    Email : {data.get('client_email', '')}
                </div>
            </div>

            <hr>
            <h3 style="text-align:center; margin:10px 0;">REÇU DE PAIEMENT</h3>

            <p><b>Objet :</b> {data['objet']}</p>
            <p><b>Montant payé :</b> {data['amount']:.2f} FCFA</p>

            <hr>
            <div style="display:flex; justify-content:flex-end; align-items:center; gap:10px; margin-top:20px;">
                <p style="margin:0;">Fait à Bamako, le {today}</p>
                <img src="{signature_path}" width="220">
            </div>

            {footer_text}
        </div>
        """
        return html
