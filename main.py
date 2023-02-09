import streamlit as st
from PIL import Image
#Dictionary with acronyms
#CHeck NO DATA and # to fill this info. The ones without acronyms are not on these dictionary either
dict = {"1N":["One Network","Collaboration Platform"],"3POI":["Third- Party Owned Inventory","#"],
        "API":["Application Programming Interface","Mechanisms that enable two or more computer programs to communicate with each each other using a set of definitions and protocols"],
        "APS":["Advanced Planning System","#"], "ASN":["Advanced Shipping Notice","EDI message sent from the shipper to the receiver prior to the departure of the shipment from the shipper`s facility."],
        "AWS":["Amazone Web Services","#"], "B/S":["Buy/Sell","HPE process to Buy materials from SUP and sell it to RSP"], "BOA":["Business Owned Applications","Power BI, QlikSense, Tableau Tools"],
        "BOD":["Bill of Distribution","#"], "BOM":["Bill of Materials","#"], "BPO":["Business Process Owners", "#"], "BRD":["Business Requirement Documents","#"],"CRM":["Customer Relationship Management","#"],
        "CV%":["Percent os Coefficient Variability","#"], "CVTP":["CV Time Phase", "#"], "EDI":["Electronic Data Interchange","Computer-to computer exchange of business documents in a standard electronic format between business partners."],
        "EMDM":["NO DATA","Customer Hierarchy Data"], "ERP":["Enterprise Resource Planning","#"], "FC":["Forecast", "Testying of an application to ensure it meets business needs"],"FDS":["Functional Design Document","#"],
        "HPEOI":["HPE Owned Inventory","#"], "IBP":["Integrated Business Planning","#"], "IIH":["Inbound Inventory Hub","#"],"MRP":["Material Requirements Planning","A system to plan manufacturing production."],
        "MTP":["Move to Production","#"], "ODM":["Original Design Manufacturer","#"],"PGI":["Post Good Issue","#"],"PIR":["Purchasing info Records","An association of material and a vendor"],
        "PO":["Purchase order","#"], "PPS":["Pick, Pack & Ship","#"], "RPA":["Robotic Process Automation","#"], "RSD":["Request Ship Date","Customer requested shipment initiation date for delivery"],
        "RSP":["Regional Service Provider","Outside HPE Manufacturers (Outsorce Manufacturer)"], "RVC":["Regional Value Services","Internal HPE Manufacturer"],
        "S&OP":["Sales and Operation Planning","Integrated palnning process that aligns demand, supply, and financial planning and is managed as pasrt of a company`s master planning"],
        "SERP":["Single Enterprise Resourece Planning","S4, SAP, HANA"], "SFDC":["Salesforce DotCom","#"],"SFTP":["Secure File Transfer Protocol","File protocol for transfering large files over the web."],
        "SIT":["System Integration Testing","Testing of an application to ensure it meets its engineering specifications"],
        "SOW":["Statement of Work", "Formal document that defines the entire scope of work involved for a vendor and clarifies deliverables, costs, and timeline"],
        "SS":["Safety Stock","#"], "SUP":["Suppliers","#"], "TDS":["Technical Design Document","#"], "UAT":["User Aceptance Testing","#"], "USCV":["Upstream Supply Chain Visibility","#"],
        "VT":["Virtual Theater","#"], "WIP":["Work in Progress","#"], "WOS":["Weeks of Supply","#"], "EAP":["Enterprise Analytics Plataform","AKA Data Lake"]
        }


#La Web app
img = Image.open("img.png")
st.image(img)
st.title("We want to simplify things for you: ")
st.subheader("Enter the acronym you wish to consult")
st.text("The idea is that this web app will help you make your entry into the company as well as\n"
        " effectively consult the thousands of acronyms that the company uses.")


sig = st.text_input("Place the acronyms here:")
sig = sig.upper()
if sig in dict:
        #var = "Las siglas "+ sig +" significan: "+dict[sig(0)]
        #ver = print(var)
        st.write("The acronym **:blue[", sig,"]** means: \n**:blue[",dict[sig][0],"]**")
        st.subheader(dict[sig][0])
        st.write(":blue[A brief description would be: ]")
        if dict[sig][1] == "#":
                st.write(":red[There is not a brief description yet on the database.]")
        else:
                st.subheader(dict[sig][1])

elif sig not in dict:
        st.error("These acronyms are not in the database, please check.")
else:
        st.caption("Type the acronym you wish to search for and press enter to continue.")
