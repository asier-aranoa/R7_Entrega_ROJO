def resultado(act_cor,act_no_cor,patri_neto,pasivo_cor,pasivo_no_cor,roa,roe,
act_cor_1,act_no_cor_1,patri_neto_1,pasivo_cor_1,pasivo_no_cor_1,roa_1,roe_1,
act_cor_2,act_no_cor_2,patri_neto_2,pasivo_cor_2,pasivo_no_cor_2,roa_2,roe_2,
act_cor_3,act_no_cor_3,patri_neto_3,pasivo_cor_3,pasivo_no_cor_3,roa_3,roe_3):

    Fondo_de_maniobra = act_cor - pasivo_cor
    ratio_de_liquidez = act_cor/pasivo_cor
    Ratio_de_endeudamiento = (pasivo_no_cor+ pasivo_cor)/patri_neto
    Ratio_de_endeudamiento_a_largo_plazo = pasivo_no_cor/patri_neto
    Ratio_de_deuda = (pasivo_no_cor + pasivo_cor)/(act_cor+act_no_cor)
    Ratio_de_apalancamiento_financiero = (act_cor+act_no_cor)/patri_neto
    ROA = roa
    ROE= roe
    Fondo_de_maniobra_1 = act_cor_1 - pasivo_cor_1
    ratio_de_liquidez_1 = act_cor_1/pasivo_cor_1
    Ratio_de_endeudamiento_1 = (pasivo_no_cor_1+ pasivo_cor_1)/patri_neto_1
    Ratio_de_endeudamiento_a_largo_plazo_1 = pasivo_no_cor_1/patri_neto_1
    Ratio_de_deuda_1 = (pasivo_no_cor_1 + pasivo_cor_1)/(act_cor_1+act_no_cor_1)
    Ratio_de_apalancamiento_financiero_1 = (act_cor_1+act_no_cor_1)/patri_neto_1
    ROA_1 = roa_1
    ROE_1= roe_1
    Fondo_de_maniobra_2 = act_cor_2 - pasivo_cor_2
    ratio_de_liquidez_2 = act_cor_2/pasivo_cor_2
    Ratio_de_endeudamiento_2 = (pasivo_no_cor_2+ pasivo_cor_2)/patri_neto_2
    Ratio_de_endeudamiento_a_largo_plazo_2 = pasivo_no_cor_2/patri_neto_2
    Ratio_de_deuda_2 = (pasivo_no_cor_2 + pasivo_cor_2)/(act_cor_2+act_no_cor_2)
    Ratio_de_apalancamiento_financiero_2 = (act_cor_2+act_no_cor_2)/patri_neto_2
    ROA_2 = roa_2
    ROE_2= roe_2
    Fondo_de_maniobra_3 = act_cor_3 - pasivo_cor_3
    ratio_de_liquidez_3 = act_cor_3/pasivo_cor_3
    Ratio_de_endeudamiento_3 = (pasivo_no_cor_3+ pasivo_cor_3)/patri_neto_3
    Ratio_de_endeudamiento_a_largo_plazo_3 = pasivo_no_cor_3/patri_neto_3
    Ratio_de_deuda_3 = (pasivo_no_cor_3 + pasivo_cor_3)/(act_cor_3+act_no_cor_3)
    Ratio_de_apalancamiento_financiero_3 = (act_cor_3+act_no_cor_3)/patri_neto_3
    ROA_3 = roa_3
    ROE_3 = roe_3

    return(Fondo_de_maniobra,Fondo_de_maniobra_1,Fondo_de_maniobra_2,Fondo_de_maniobra_3,
    ROA,ROA_1,ROA_2,ROA_3,
    ROE,ROE_1,ROE_2,ROE_3,
    Ratio_de_apalancamiento_financiero,Ratio_de_apalancamiento_financiero_1,Ratio_de_apalancamiento_financiero_2,Ratio_de_apalancamiento_financiero_3,
    Ratio_de_deuda,Ratio_de_deuda_1,Ratio_de_deuda_2,Ratio_de_deuda_3,
    Ratio_de_endeudamiento,Ratio_de_endeudamiento_1,Ratio_de_endeudamiento_2,Ratio_de_endeudamiento_3,
    Ratio_de_endeudamiento_a_largo_plazo,Ratio_de_endeudamiento_a_largo_plazo_1,Ratio_de_endeudamiento_a_largo_plazo_2,Ratio_de_endeudamiento_a_largo_plazo_3,
    ratio_de_liquidez,ratio_de_liquidez_1,ratio_de_liquidez_2,ratio_de_liquidez_3)




