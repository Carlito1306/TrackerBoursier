#!/usr/bin/env python3
import streamlit as st
import yfinance

TICKERS = sorted(list(set([
    "AAPL","MSFT","GOOGL","GOOG","AMZN","NVDA","META","TSLA","BRK-B","UNH","JNJ","JPM","V","PG","XOM","MA","HD","CVX","MRK","ABBV","LLY","PEP","KO","PFE","COST","TMO","AVGO","MCD","WMT","CSCO","ABT","ACN","DHR","NEE","VZ","ADBE","NKE","TXN","PM","CRM","UNP","RTX","CMCSA","BMY","ORCL","HON","QCOM","T","LOW","UPS","MS","SPGI","GS","BA","CAT","SBUX","IBM","INTC","AMD","INTU","GE","BLK","AMGN","DE","GILD","AXP","MDLZ","ADI","ISRG","CVS","BKNG","TMUS","PLD","SYK","VRTX","REGN","ADP","LRCX","MMC","CI","ZTS","CB","NOW","SCHW","MO","SO","BDX","DUK","EOG","CL","CME","ITW","SLB","NOC","CSX","FDX","ICE","WM","PNC","EQIX","APD","MU","AON","BSX","SHW","ETN","NSC","TGT","FCX","ATVI","EMR","HUM","GM","ORLY","PSX","KLAC","MCK","AZO","PXD","MCHP","MAR","SNPS","GD","OXY","CDNS","MET","TRV","F","SRE","AEP","APH","DLR","FTNT","TEL","ROP","AIG","PSA","MSCI","HES","CCI","PAYX","AFL","TFC","WELL","NEM","AJG","KMB","STZ","D","O","A","SPG","CMG","ROST","PRU","GIS","YUM","HSY","CTVA","ALL","FAST","CTAS","KR","PCAR","BK","OKE","CMI","EA","MNST","IDXX","ADM","DXCM","BIIB","DVN","KHC","ODFL","ANET","DHI","LHX","VRSK","PEG","EXC","IQV","HAL","ED","CTSH","VICI","MTD","CSGP","GWW","EW","XEL","FANG","AME","DLTR","KEYS","DOW","WEC","ANSS","RMD",
    "PANW","CRWD","DDOG","ZS","NET","SNOW","PLTR","COIN","MSTR","ROKU","ZM","DOCU","OKTA","TWLO","TTD","DASH","ABNB","PYPL","SQ","SHOP","MELI","SE","GRAB","RIVN","LCID","NIO","XPEV","LI","NKLA","FSR","SOFI","HOOD","UPST","AFRM","RBLX","U","MTTR","PATH","AI","BBAI","ASAN","MDB","ESTC","CFLT","GTLB","DOCN","HUBS","WDAY","VEEV","TEAM","SPLK","NTNX","SMAR","APP","BILL","PCTY","PAYC","FIVN","NICE","MANH","SSNC","GLOB","EPAM","WIX","ETSY","EBAY","W","CHWY","CVNA","CARG","CPRT","POOL","ULTA","LULU","DECK","CROX","BIRD","ONON","SKX","NFLX","DIS","WBD","PARA","CHTR","FOXA","NWSA","NYT","OMC","IPG","MGNI","PUBM","DV","IAS","ZETA","BRZE","SEMR","APPS","JAMF",
    "RY.TO","TD.TO","BMO.TO","BNS.TO","CM.TO","NA.TO","MFC.TO","SLF.TO","GWO.TO","IAG.TO","POW.TO","FFH.TO","IFC.TO","EQB.TO","CWB.TO","LB.TO","GSY.TO","X.TO","CF.TO","DFY.TO","ENB.TO","TRP.TO","PPL.TO","KEY.TO","IPL.TO","GEI.TO","SPB.TO","ARX.TO","ERF.TO","BIR.TO","CNQ.TO","SU.TO","CVE.TO","IMO.TO","OVV.TO","MEG.TO","TOU.TO","WCP.TO","BTE.TO","CR.TO","CP.TO","CNR.TO","QBR-B.TO","TFII.TO","AND.TO","GFL.TO","WSP.TO","STN.TO","ARE.TO","BDT.TO","SHOP.TO","CSU.TO","OTEX.TO","DCBO.TO","KXS.TO","ENGH.TO","TOI.TO","NVEI.TO","LSPD.TO","REAL.TO","BB.TO","TIXT.TO","ALYA.TO","QIPT.TO","PHO.TO","DSG.TO","EGLX.TO","FOBI.TO","MTRX.TO","XBC.TO","ABX.TO","K.TO","AEM.TO","FNV.TO","WPM.TO","AGI.TO","YRI.TO","KNT.TO","NG.TO","SVM.TO","BCE.TO","T.TO",
    "SPY","VOO","IVV","VTI","QQQ","QQQM","VGT","XLK","SMH","SOXX","ARKK","ARKG","ARKW","ARKF","ARKQ","SOXL","TQQQ","SPXL","UPRO","TECL","SOXS","SQQQ","SPXS","SDOW","TZA","UVXY","VXX","SVXY","VIXY","VIXM","DIA","IWM","IWF","IWD","IJH","IJR","VB","VBR","VBK","VO","VTV","VUG","SCHD","VIG","DVY","DGRO","VYM","HDV","SPYD","SPHD","XLF","XLE","XLV","XLY","XLP","XLI","XLU","XLB","XLRE","XLC","GLD","SLV","GDX","GDXJ","IAU","PPLT","PALL","USO","UNG","DBA","TLT","IEF","SHY","BND","AGG","LQD","HYG","JNK","EMB","TIP","VWO","EEM","IEMG","VEA","EFA","IEFA","VXUS","VEU","IXUS","ACWI","KWEB","FXI","MCHI","ASHR","EWJ","EWZ","EWY","EWT","INDA","VNM",
    "XIU.TO","XIC.TO","VCN.TO","ZCN.TO","HXT.TO","XMD.TO","XCS.TO","ZLB.TO","ZLU.TO","ZDV.TO","XQQ.TO","ZQQ.TO","ZNQ.TO","TEC.TO","HXQ.TO","XUS.TO","VFV.TO","ZSP.TO","VSP.TO","HXS.TO","XEQT.TO","XGRO.TO","XBAL.TO","VGRO.TO","VBAL.TO","VEQT.TO","ZGRO.TO","ZBAL.TO","ZEQT.TO","HGRO.TO","XEF.TO","VIU.TO","ZEA.TO","VXC.TO","XAW.TO","ZEM.TO","VEE.TO","XEM.TO","ZDM.TO","HXDM.TO","XSP.TO","ZUE.TO","VUN.TO","ZUQ.TO","ZWC.TO","ZWB.TO","ZWK.TO","ZWU.TO","ZWH.TO","ZWG.TO",
    "BTC-USD","ETH-USD","SOL-USD","XRP-USD","ADA-USD","DOGE-USD","AVAX-USD","DOT-USD","MATIC-USD","LINK-USD","ATOM-USD","UNI-USD","LTC-USD","BCH-USD","NEAR-USD","APT-USD","FIL-USD","ARB-USD","OP-USD","INJ-USD","GBTC","ETHE","BITO","IBIT","FBTC","ARKB","BITB","HODL","EZBC","BTCO","RIOT","MARA","CLSK","HUT","BITF","HIVE","BTBT","CIFR",
    "WFC","BAC","C","USB","BX","KKR","APO","CG","ARES","OWL","TPG","VCTR","HLNE","STEP","IBKR","VIRT","NDAQ","CBOE","TW","MKTX","COF","DFS","SYF","LC","ALLY","CACC"
])))

st.set_page_config(page_title="Tracker Boursier", page_icon="📈")
st.title("📈 Tracker Boursier Instantané")
st.caption(f"{len(TICKERS)} tickers disponibles")

symbole = st.selectbox("Sélectionnez un symbole :", [""] + TICKERS)

if symbole:
    ticker = yfinance.Ticker(symbole)
    data = ticker.history(period="2d")
    if len(data) >= 2:
        prix = data["Close"].iloc[-1]
        var = prix - data["Close"].iloc[-2]
        pct = (var / data["Close"].iloc[-2]) * 100
        st.metric(f"{symbole}", f"${prix:.2f}", f"{var:+.2f}$ ({pct:+.2f}%)")
        st.subheader("📊 Historique")
        p = st.selectbox("Période", ["1mo","3mo","6mo","1y","5y"], format_func=lambda x: {"1mo":"1 mois","3mo":"3 mois","6mo":"6 mois","1y":"1 an","5y":"5 ans"}[x])
        st.line_chart(ticker.history(period=p)["Close"])
