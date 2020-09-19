from selenium.webdriver.common.by import By


class Locators:
    add_car_block_years = By.CSS_SELECTOR, '.add-car-block .garage-dd-toggler:nth-child(1)'
    add_car_block_manufactures = By.CSS_SELECTOR, '.add-car-block .garage-dd-toggler:nth-child(2)'
    add_car_block_models = By.CSS_SELECTOR, '.add-car-block .garage-dd-toggler:nth-child(3)'
    add_car_block_type_models = By.CSS_SELECTOR, '.add-car-block .garage-dd-toggler:nth-child(4)'
    add_car_block_modifications = By.CSS_SELECTOR, '.add-car-block .garage-dd-toggler:nth-child(5)'

    btn_blue = By.CLASS_NAME, 'btn-blue'
    btn_green = By.CLASS_NAME, 'btn-green'
    button_increment = By.CSS_SELECTOR, 'button[aria-label="increment"]'
    button_decrement = By.CSS_SELECTOR, 'button[aria-label="decrement"]'
    button_trash = By.XPATH, '//*[@name="trash"]/../..'
    button_checkout = By.CSS_SELECTOR, 'a[href = "/checkout/"]'
    button_to_cart = By.CSS_SELECTOR, '.buttons a[href = "/cart/"]'
    btn_icon = By.CLASS_NAME, 'btn-icon'
    button_car_controls_edit = By.CSS_SELECTOR, 'button[class="car-controls-edit"]'

    breadcrumbs_current_path = By.CLASS_NAME, 'breadcrumbs-current-path'
    breadcrumbs_devider = By.CLASS_NAME, 'breadcrumbs-divider'
    breadcrumbs = By.CSS_SELECTOR, '.breadcrumbs a'

    car_descendants_wrapper_h2 = By.CSS_SELECTOR, '.car-descendants-wrapper h2'
    car_descendants_wrapper_a = By.CSS_SELECTOR, '.car-descendants-wrapper a'
    car_year = By.CLASS_NAME, 'car-year'
    car_vin = By.CLASS_NAME, 'car-vin'
    car_name = By.CLASS_NAME, 'car-name'
    carVIN_field = By.CSS_SELECTOR, 'input[aria-label = "carVIN"]'
    carYear_field = By.CSS_SELECTOR, 'input[aria-label = "carYear"]'
    car_year_block_button = By.CSS_SELECTOR, '.car-year-block button[name = "{}"]'
    car_manufacture_block_input = By.CSS_SELECTOR, '.car-manufacture-block input'
    car_model_wrapper_button = By.CSS_SELECTOR, '.car-model-wrapper button[name = "{}"]'
    car_model_type_block_button = By.CSS_SELECTOR, '.car-model-type-block button[name = "{}"]'
    car_modification_block_tr = By.CSS_SELECTOR, '.car-modification-block tr[data-name = "{}"]'
    cart_remove = By.CLASS_NAME, 'cart-remove'

    car_controls_edit_button = By.CSS_SELECTOR, 'button[class="car-controls-edit"]'
    carVIN_button_ok = By.CSS_SELECTOR, 'input[aria-label = "carVIN"]~button'
    carYear_button_ok = By.CSS_SELECTOR, 'input[aria-label = "carYear"]~button'
    cart_price = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title span'
    catalogue_list_price = By.CSS_SELECTOR, '.catalogue-list .price'
    catalogue_list_name = By.CSS_SELECTOR, '.catalogue-list strong'
    catalogue_list_brand = By.CSS_SELECTOR, '.catalogue-list .trademark span'
    catalogue_list_vendor_code = By.CSS_SELECTOR, '.catalogue-list .trademark'
    catalogue_list_delivery = By.CSS_SELECTOR, '.catalogue-list .delivery'

    description = By.CSS_SELECTOR, 'meta[name = "description"]'


    chosen_car_info_vin = By.XPATH, '//div[@class = "chosen-car-info"]//div[contains(text(), "VIN")]'
    container_our_cities = By.CSS_SELECTOR, 'div[class = "container text-container"]'

    grid_table_first_offer_price = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .price'
    grid_table_first_offer_name = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) td:nth-child(2)'
    grid_table_first_offer_brand = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .name strong'
    grid_table_first_offer_delivery = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .delivery'
    grid_table_first_offer_vendor_code = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .name a'
    grid_table_first_offer_button_blue = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .btn-blue'
    grid_table_first_offer_button_green = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1) .btn-green'
    grid_table_first_offers = By.CSS_SELECTOR, '.grid-table tr[class = "     "]:nth-child(1)'
    grid_table_price = By.CSS_SELECTOR, '.grid-table .price'
    grid_table_name = By.CSS_SELECTOR, '.grid-table .name-inner p'
    grid_table_brand = By.CSS_SELECTOR, '.grid-table .name>strong'
    grid_table_vendor_code = By.CSS_SELECTOR, '.grid-table .name a strong'
    grid_table_delivery_date = By.CSS_SELECTOR, '.grid-table .delivery, .grid-table .exists'
    grid_table_price_sum = By.CSS_SELECTOR, '.grid-table .total'

    # my_car_empty = By.CLASS_NAME, 'garage'
    garage = By.CLASS_NAME, 'garage'
    # my_car_with_car = By.CSS_SELECTOR, '.garage  div[title = "Выбранный автомобиль"]'
    garage_selected_car = By.CSS_SELECTOR, '.garage  div[title = "Выбранный автомобиль"]'
    garage_dd_content_button_blue = By.CSS_SELECTOR, '.garage-dd-content .btn-blue'

    garage_add_car_years = By.CSS_SELECTOR, '.garage-add-car .garage-dd-toggler:nth-child(1)'
    garage_add_car_manufactures = By.CSS_SELECTOR, '.garage-add-car .garage-dd-toggler:nth-child(2)'
    garage_add_car_models = By.CSS_SELECTOR, '.garage-add-car .garage-dd-toggler:nth-child(3)'
    garage_add_car_type_models = By.CSS_SELECTOR, '.garage-add-car .garage-dd-toggler:nth-child(4)'
    garage_add_car_modifications = By.CSS_SELECTOR, '.garage-add-car .garage-dd-toggler:nth-child(5)'

    garage_car_list_vin = By.XPATH, '//div[@class = "garage-car-list"]//li/div[contains(text(), "VIN")]'
    garage_car_list_a = By.CSS_SELECTOR, '.garage-car-list a'
    general_info_delivery = By.CSS_SELECTOR, '.general-info .delivery'

    guide_tabs = By.CSS_SELECTOR, '.guide-tabs .react-tabs__tab-list li'
    guide_tab_selected = By.CSS_SELECTOR, '.guide-tabs li[aria-selected = "true"]'

    h1 = By.TAG_NAME, 'h1'
    header_contact_nav = By.CSS_SELECTOR, '.header-contact-nav a'

    info_block_wrapper_price = By.CSS_SELECTOR, '.info-block-wrapper .price'
    info_block_wrapper_name = By.CSS_SELECTOR, '.info-block-wrapper .title-wrapper .bold'
    info_block_wrapper_brand = By.CSS_SELECTOR, '.info-block-wrapper .trademark span'
    info_block_wrapper_vendor_code = By.CSS_SELECTOR, '.info-block-wrapper .trademark'
    info_block_wrapper_delivery = By.CSS_SELECTOR, '.info-block-wrapper .delivery'
    info_block_price = By.CSS_SELECTOR, '.info-block .price'
    info_block_name = By.CSS_SELECTOR, '.info-block .title'
    info_block_brand = By.CSS_SELECTOR, '.info-block .trademark span'
    info_block_vendor_code = By.CSS_SELECTOR, '.info-block .trademark'
    info_block_delivery = By.CSS_SELECTOR, '.info-block .delivery'
    info_block_button_blue = By.CSS_SELECTOR, '.info-block-wrapper .btn-blue'
    info_block_button_green = By.CSS_SELECTOR, '.info-block-wrapper .btn-green'

    lang_dd_button_button = By.CSS_SELECTOR, '.lang-dd-button button'
    lang_select_button = By.CSS_SELECTOR, '.lang-select button'
    list_item_button_blue = By.CSS_SELECTOR, '.list-item-btns .btn-blue'
    list_item_button_green = By.CSS_SELECTOR, '.list-item-btns .btn-green'

    manufacture_list_button = By.CSS_SELECTOR, '.manufacture-list button'

    modal_grid_price = By.CSS_SELECTOR, '.modal-grid .total'
    modal_grid_name = By.CSS_SELECTOR, '.modal-grid .name-inner p'
    modal_grid_brand = By.CSS_SELECTOR, '.modal-grid .name>strong'
    modal_grid_vendor_code = By.CSS_SELECTOR, '.modal-grid .name a strong'
    modal_grid_delivery = By.CSS_SELECTOR, '.modal-grid .delivery, .modal-grid .exists'

    mega_menu_link = By.CLASS_NAME, 'mega-menu-link'

    name_inner_vendor_code = By.CSS_SELECTOR, '.name-inner a strong'
    name_inner_name = By.CSS_SELECTOR, '.name-inner p'
    name_inner_brand = By.CSS_SELECTOR, '.name-inner .name>strong'

    nested_row_0_button_blue = By.CSS_SELECTOR, '.nested-row-0:nth-child(1) .btn-blue'
    nested_row_0_button_green = By.CSS_SELECTOR, '.nested-row-0:nth-child(1) .btn-green'
    nested_row_0_price = By.CSS_SELECTOR, '.nested-row-0:nth-child(1) .price'
    nested_row_0_vendor_code = By.CSS_SELECTOR, '.nested-row-0:nth-child(1) .name-inner a strong'
    nested_row_0_name = By.CSS_SELECTOR, '.nested-row-0:nth-child(1) .name-inner p'
    nested_row_0_brand = By.CSS_SELECTOR, '.nested-row-0:nth-child(1) .name-inner .name>strong'
    nested_row_0_delivery = By.CSS_SELECTOR, '.nested-row-0:nth-child(1) .general-info .delivery'

    popular_manufactures = By.CSS_SELECTOR, '.popular-manufactures-container a'
    popular_models = By.CSS_SELECTOR, '.popular-models-block a'
    popular_categories = By.CSS_SELECTOR, '.popular-categories-container a'

    product_short_info_price = By.CSS_SELECTOR, '.product-short-info .price'
    product_short_info_delivery = By.CSS_SELECTOR, '.product-short-info .delivery'
    product_attributes_values = By.CSS_SELECTOR, '.product-attributes a'

    phone_field = By.ID, 'phone-field'

    password_field = By.NAME, 'password'

    preloader = By.CLASS_NAME, 'preloader '
    preloader_icon = By.CSS_SELECTOR, '.preloader.visible'

    price_wrapper_price = By.CSS_SELECTOR, '.price-wrapper .price'
    price_wrapper_button_blue = By.CSS_SELECTOR, '.price-wrapper .btn-blue'
    price_wrapper_button_green = By.CSS_SELECTOR, '.price-wrapper .btn-green'

    quantity_field = By.CSS_SELECTOR, '.quantity-field input'

    short_info_block_brand = By.CSS_SELECTOR, '.short-info-block .bold:first-child'
    short_info_block_vendor_code = By.CSS_SELECTOR, '.short-info-block .bold:nth-child(2)'

    seo_text = By.CLASS_NAME, 'seo-text'

    title_block = By.CLASS_NAME, 'block-title'

    total_wrapper_price_total = By.CSS_SELECTOR, '.total-wrapper .total'

    user_title_username = By.CSS_SELECTOR, '.user-title span'

    user_menu_toggler = By.CLASS_NAME, 'user-menu-toggler '
    user_menu_toggler_inner_cart_count = By.CSS_SELECTOR, '.user-menu-toggler-inner .icon .cart-count span'

    user_change_counterparty_button = By.CSS_SELECTOR, '.user-change-counterparty button'

    # special locators
    cart_with_items = By.CSS_SELECTOR, '.cart .lowerCase .user-menu-title'
    cart_without_items = By.CSS_SELECTOR, '.cart .user-menu-title'
    my_car_empty = By.CLASS_NAME, 'garage'
    my_car_selected_car = By.CSS_SELECTOR, '.garage  div[title = "Выбранный автомобиль"]'
    profile_anonim = By.CSS_SELECTOR, '.profile button'
    profile_avtorpol = By.CSS_SELECTOR, '.profile .colored .user-menu-title'
