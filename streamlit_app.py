#!/usr/bin/env python3
"""Application Web Streamlit de suivi boursier en temps quasi-réel."""

import streamlit as st
import yfinance
import pandas as pd

# =============================================================================
# BASE DE DONNÉES : 500 TICKERS
# =============================================================================

TICKERS_SP500: list[str] = [
    "AAPL", "MSFT", "GOOGL", "GOOG", "AMZN", "NVDA", "META", "TSLA", "BRK-B", "UNH",
    "JNJ", "JPM", "V", "PG", "XOM", "MA", "HD", "CVX", "MRK", "ABBV",
    "LLY", "PEP", "KO", "PFE", "COST", "TMO", "AVGO", "MCD", "WMT", "CSCO",
    "ABT", "ACN", "DHR", "NEE", "VZ", "ADBE", "NKE", "TXN", "PM", "CRM",
    "UNP", "RTX", "CMCSA", "BMY", "ORCL", "HON", "QCOM", "T", "LOW", "UPS",
    "MS", "SPGI", "GS", "BA", "CAT", "SBUX", "IBM", "INTC", "AMD", "INTU",
    "GE", "BLK", "AMGN", "DE", "GILD", "AXP", "MDLZ", "ADI", "ISRG", "CVS",
    "BKNG", "TMUS", "PLD", "SYK", "VRTX", "REGN", "ADP", "LRCX", "MMC", "CI",
    "ZTS", "CB", "NOW", "SCHW", "MO", "SO", "BDX", "DUK", "EOG", "CL",
    "CME", "ITW", "SLB", "NOC", "CSX", "FDX", "ICE", "WM", "PNC", "EQIX",
    "APD", "MU", "AON", "BSX", "SHW", "ETN", "NSC", "TGT", "FCX", "ATVI",
    "EMR", "HUM", "GM", "ORLY", "PSX", "KLAC", "MCK", "AZO", "PXD", "MCHP",
    "MAR", "SNPS", "GD", "OXY", "CDNS", "MET", "TRV", "F", "SRE", "AEP",
    "APH", "DLR", "FTNT", "TEL", "ROP", "AIG", "PSA", "MSCI", "HES", "CCI",
    "PAYX", "AFL", "TFC", "WELL", "NEM", "AJG", "KMB", "STZ", "D", "O",
    "A", "SPG", "CMG", "ROST", "PRU", "GIS", "YUM", "HSY", "CTVA", "ALL",
    "FAST", "CTAS", "KR", "PCAR", "BK", "OKE", "CMI", "EA", "MNST", "IDXX",
    "ADM", "DXCM", "BIIB", "DVN", "KHC", "ODFL", "ANET", "DHI", "LHX", "VRSK",
    "PEG", "EXC", "IQV", "HAL", "ED", "CTSH", "VICI", "MTD", "CSGP", "GWW",
    "EW", "XEL", "FANG", "AME", "DLTR", "KEYS", "DOW", "WEC", "ANSS", "RMD",
]

TICKERS_NASDAQ: list[str] = [
    "PANW", "CRWD", "DDOG", "ZS", "NET", "SNOW", "PLTR", "COIN", "MSTR", "ROKU",
    "ZM", "DOCU", "OKTA", "TWLO", "TTD", "DASH", "ABNB", "PYPL", "SQ", "SHOP",
    "MELI", "SE", "GRAB", "RIVN", "LCID", "NIO", "XPEV", "LI", "NKLA", "FSR",
    "SOFI", "HOOD", "UPST", "AFRM", "RBLX", "U", "MTTR", "PATH", "AI", "BBAI",
    "ASAN", "MDB", "ESTC", "CFLT", "GTLB", "DOCN", "HUBS", "WDAY", "VEEV", "TEAM",
    "SPLK", "NTNX", "SMAR", "APP", "BILL", "PCTY", "PAYC", "FIVN", "NICE", "MANH",
    "SSNC", "GLOB", "EPAM", "WIX", "ETSY", "EBAY", "W", "CHWY", "CVNA", "CARG",
    "CPRT", "POOL", "ULTA", "LULU", "DECK", "CROX", "BIRD", "ONON", "SKX", "NKE",
    "NFLX", "DIS", "WBD", "PARA", "CMCSA", "CHTR", "FOXA", "NWSA", "NYT", "OMC",
    "IPG", "MGNI", "PUBM", "DV", "IAS", "ZETA", "BRZE", "SEMR", "APPS", "JAMF",
]

TICKERS_TSX: list[str] = [
    "RY.TO", "TD.TO", "BMO.TO", "BNS.TO", "CM.TO", "NA.TO", "MFC.TO", "SLF.TO", "GWO.TO", "IAG.TO",
    "POW.TO", "FFH.TO", "IFC.TO", "EQB.TO", "CWB.TO", "LB.TO", "GSY.TO", "X.TO", "CF.TO", "DFY.TO",
    "ENB.TO", "TRP.TO", "PPL.TO", "KEY.TO", "IPL.TO", "GEI.TO", "SPB.TO", "ARX.TO", "ERF.TO", "BIR.TO",
    "CNQ.TO", "SU.TO", "CVE.TO", "IMO.TO", "OVV.TO", "MEG.TO", "TOU.TO", "WCP.TO", "BTE.TO", "CR.TO",
    "CP.TO", "CNR.TO", "QBR-B.TO", "TFII.TO", "AND.TO", "GFL.TO", "WSP.TO", "STN.TO", "ARE.TO", "BDT.TO",
    "SHOP.TO", "CSU.TO", "OTEX.TO", "DCBO.TO", "KXS.TO", "ENGH.TO", "TOI.TO", "NVEI.TO", "LSPD.TO", "REAL.TO",
    "BB.TO", "TIXT.TO", "ALYA.TO", "QIPT.TO", "PHO.TO", "DSG.TO", "EGLX.TO", "FOBI.TO", "MTRX.TO", "XBC.TO",
    "ABX.TO", "K.TO", "AEM.TO", "FNV.TO", "WPM.TO", "AGI.TO", "YRI.TO", "KNT.TO", "NG.TO", "SVM.TO",
]

TICKERS_ETFS_US: list[str] = [
    "SPY", "VOO", "IVV", "VTI", "QQQ", "QQQM", "VGT", "XLK", "SMH", "SOXX",
    "ARKK", "ARKG", "ARKW", "ARKF", "ARKQ", "SOXL", "TQQQ", "SPXL", "UPRO", "TECL",
    "SOXS", "SQQQ", "SPXS", "SDOW", "TZA", "UVXY", "VXX", "SVXY", "VIXY", "VIXM",
    "DIA", "IWM", "IWF", "IWD", "IJH", "IJR", "VB", "VBR", "VBK", "VO",
    "VTV", "VUG", "SCHD", "VIG", "DVY", "DGRO", "VYM", "HDV", "SPYD", "SPHD",
    "XLF", "XLE", "XLV", "XLY", "XLP", "XLI", "XLU", "XLB", "XLRE", "XLC",
    "GLD", "SLV", "GDX", "GDXJ", "IAU", "PPLT", "PALL", "USO", "UNG", "DBA",
    "TLT", "IEF", "SHY", "BND", "AGG", "LQD", "HYG", "JNK", "EMB", "TIP",
    "VWO", "EEM", "IEMG", "VEA", "EFA", "IEFA", "VXUS", "VEU", "IXUS", "ACWI",
    "KWEB", "FXI", "MCHI", "ASHR", "EWJ", "EWZ", "EWY", "EWT", "INDA", "VNM",
]

TICKERS_ETFS_CA: list[str] = [
    "XIU.TO", "XIC.TO", "VCN.TO", "ZCN.TO", "HXT.TO", "XMD.TO", "XCS.TO", "ZLB.TO", "ZLU.TO", "ZDV.TO",
    "XQQ.TO", "ZQQ.TO", "ZNQ.TO", "TEC.TO", "HXQ.TO", "XUS.TO", "VFV.TO", "ZSP.TO", "VSP.TO", "HXS.TO",
    "XEQT.TO", "XGRO.TO", "XBAL.TO", "VGRO.TO", "VBAL.TO", "VEQT.TO", "ZGRO.TO", "ZBAL.TO", "ZEQT.TO", "HGRO.TO",
    "XEF.TO", "VIU.TO", "ZEA.TO", "VXC.TO", "XAW.TO", "ZEM.TO", "VEE.TO", "XEM.TO", "ZDM.TO", "HXDM.TO",
    "XSP.TO", "ZUE.TO", "VUN.TO", "ZUQ.TO", "ZWC.TO", "ZWB.TO", "ZWK.TO", "ZWU.TO", "ZWH.TO", "ZWG.TO",
]

TICKERS_CRYPTO_AUTRES: list[str] = [
    "COIN", "MSTR", "RIOT", "MARA", "CLSK", "HUT", "BITF", "HIVE", "BTBT", "CIFR",
    "SOS", "CAN", "GBTC", "ETHE", "BITO", "BTF", "XBTF", "BITI", "ARKB", "IBIT",
    "FBTC", "BTCO", "HODL", "BITB", "EZBC", "BRRR", "BTCW", "DEFI", "BLOK", "LEGR",
    "V", "MA", "PYPL", "SQ", "AFRM", "SOFI", "UPST", "LC", "ALLY", "CACC",
    "AXP", "COF", "DFS", "SYF", "WFC", "BAC", "C", "USB", "PNC", "TFC",
    "BX", "KKR", "APO", "CG", "ARES", "OWL", "TPG", "VCTR", "HLNE", "STEP",
    "SCHW", "IBKR", "HOOD", "VIRT", "NDAQ", "ICE", "CME", "CBOE", "TW", "MKTX",
]

# Assemblage de tous les tickers (dédupliqués)
TOUS_LES_TICKERS: list[str] = sorted(list(set(
    TICKERS_SP500 +
    TICKERS_NASDAQ +
    TICKERS_TSX +
    TICKERS_ETFS_US +
    TICKERS_ETFS_CA +
    TICKERS_CRYPTO_AUTRES
)))


# =============================================================================
# FONCTION PRINCIPALE
# =============================================================================

def obtenir_prix_recent(symbole: str) -> dict[str, float] | None:
    """Récupère les prix de clôture actuel et précédent pour un symbole boursier."""
    data: pd.DataFrame = yfinance.Ticker(symbole).history(period="2d")
    
    if data.empty or len(data) < 2:
        return None
    
    return {
        "prix_actuel": float(data["Close"].iloc[-1]),
        "prix_precedent": float(data["Close"].iloc[-2]),
    }


# =============================================================================
# INTERFACE STREAMLIT
# =============================================================================

st.set_page_config(
    page_title="Tracker Boursier",
    page_icon="📈",
    layout="centered",
)

st.title("📈 Tracker Boursier Instantané")
st.caption(f"{len(TOUS_LES_TICKERS)} tickers disponibles • Données via Yahoo Finance")

symbole_cherche: str = st.selectbox(
    "Sélectionnez un symbole boursier :",
    options=[""] + TOUS_LES_TICKERS,
    index=0,
    placeholder="Tapez pour rechercher (ex: AAPL, SHOP.TO, SPY)...",
)

if symbole_cherche:
    with st.spinner(f"Chargement des données pour {symbole_cherche}..."):
        try:
            donnees: dict[str, float] | None = obtenir_prix_recent(symbole_cherche)
            
            if donnees is not None:
                variation_dollars: float = donnees["prix_actuel"] - donnees["prix_precedent"]
                variation_pourcentage: float = (variation_dollars / donnees["prix_precedent"]) * 100
                
                st.metric(
                    label=f"{symbole_cherche} • Prix Actuel",
                    value=f"${donnees['prix_actuel']:.2f}",
                    delta=f"{variation_dollars:+.2f}$ ({variation_pourcentage:+.2f}%)",
                )
            else:
                st.error(
                    f"❌ Impossible de récupérer les données pour {symbole_cherche}. "
                    "Symbole invalide ou marché fermé."
                )
        except Exception as e:
            st.error(
                f"❌ Erreur de connexion pour {symbole_cherche}. "
                f"Réessayez dans quelques secondes."
            )

