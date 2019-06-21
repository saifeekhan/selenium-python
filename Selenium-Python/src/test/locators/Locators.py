'''
Created on Jun 20, 2019

@author: saif.khan
'''
class Locators():
    #########################
    # Common Wijmo Objects
    #########################
    wj_dropdown_xpath = "//div[@wj-part='dropdown']//div"
    
    #########################
    # Login Screen Objects
    #########################
    userid_text_name = "email"
    password_text_name = "password"
    login_submit_xpath="//button[@class='login_btn']"
    
    #########################
    # Home Screen Objects
    #########################
    settings_link_xpath = "//i[@class='fa fa-cog fa-lg']"
    logout_link_xpath="// a[contains(text(), 'Log Out')]"
    
    logo_img_xpath ="//img[@class='logo_img']"

    vault_menu_xpath = "//a[contains(text(),'Vault')]"
    vault_subMenu_xpath="//a[contains(text(),'Stock Deposit/Withdraw')]"

    ###########################
    # Vault Screen Objects
    ###########################
    vault_pgCaption_label_xpath = "//span[contains(text(),'Deposits / Withdrawal')]"
    vault_addStock_button_xpath = "//i[contains(@class,'fa fa-plus')]"

    # XPath of Exchange combo
    vault_exchange_input_xpath = "//wj-combo-box[@id='exchangeId']//input[@class='wj-form-control']"
    vault_exchange_combo_xpath = "//wj-combo-box[@id='exchangeId']//span[@class='wj-glyph-down']"

    # XPath of Custodian
    vault_cust_combo_xpath = "//wj-combo-box[@id='custodianId']//span[contains(@class,'wj-glyph-down')]"

    # XPath of Account combo
    vault_clientID_input_xpath = "//input[@formcontrolname='clientId']"
    vault_clientID_combo_xpath = "//wj-auto-complete[@id='clientId']//span[contains(@class,'wj-glyph-down')]"

    # XPath of Security combo
    vault_security_input_xpath = "//input[@formcontrolname='securityId']"
    vault_security_combo_xpath = "//wj-combo-box[@id='securityId']//span[contains(@class,'wj-glyph-down')]"

    # XPath of Qty input field
    vault_qty_input_xpath = "//input[@formcontrolname='quantity']"

    # XPath of Remarks field
    vault_remarks_input_xpath = "//textarea[@formcontrolname='remarks']"

    # XPath of Submit button
    vault_save_btn_xpath = "//button[@id='btnSave']"

    # XPath success message
    vault_msg_pop_xpath = "//wj-popup[@class='green_dialog wj-control wj-content wj-popup wj-state-focused']//p[contains(text(),'Record Saved Successfully.')]"
    vault_okBtn_pop_xpath = "//wj-popup[@class='green_dialog wj-control wj-content wj-popup wj-state-focused']//button[@class='btn btn-default wj-hide'][contains(text(),'Ok')]"

    # XPath of Type combo
    vault_type_combo_xpath = "//wj-combo-box[@id='entryType']//span[contains(@class,'wj-glyph-down')]"
    vault_type_item_xpath = "//div[@wj-part='dropdown']//div"