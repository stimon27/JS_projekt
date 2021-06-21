from tkinter import *
from tkinter.scrolledtext import ScrolledText
from scrapers.autocar_articles_google import scrape_autocar_articles_google
from scrapers.autocar_articles_scraper import scrape_autocar_articles
from scrapers.autoexpress_articles_google import scrape_autoexpress_articles_google
from scrapers.autoexpress_articles_scraper import scrape_autoexpress_articles
from scrapers.autoweek_articles_scraper import scrape_autoweek_articles
from scrapers.caradvice_articles_scraper import scrape_caradvice_articles
from scrapers.caranddriver_articles_google import scrape_caranddriver_articles_google
from scrapers.caranddriver_articles_scraper import scrape_caranddriver_articles
from scrapers.motor1_articles_google import scrape_motor1_articles_google
from scrapers.motor1_articles_scraper import scrape_motor1_articles
from scrapers.motortrend_articles_scraper import scrape_motortrend_articles
from scrapers.topgear_articles_google import scrape_topgear_articles_google
from scrapers.topgear_articles_scraper import scrape_topgear_articles


def gui_start():
    root = Tk()
    root.geometry('1280x720+50+50')
    root.title('Car News Web Scraper')
    root.configure(background='black')

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    main_frame = Frame(root, bg='white')
    main_frame.grid(row=0, column=0, padx=20, pady=20, sticky='NSEW')

    main_frame.rowconfigure(0, weight=2)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)
    main_frame.rowconfigure(4, weight=1)
    main_frame.rowconfigure(5, weight=1)
    main_frame.rowconfigure(6, weight=1)
    main_frame.rowconfigure(7, weight=1)
    main_frame.rowconfigure(8, weight=1)

    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=2)
    main_frame.columnconfigure(2, weight=2)
    main_frame.columnconfigure(3, weight=2)
    main_frame.columnconfigure(4, weight=1)

    welcome_label = Label(main_frame, bg='white', fg='black', text='Welcome to the car news web scraping app')
    welcome_label.config(font=('Verdana', 32))
    welcome_label.grid(row=0, column=1, columnspan=3, sticky='NSEW')

    intro_label = Label(main_frame, bg='white', fg='black', text='Choose what you want to scrape from the options below:')
    intro_label.config(font=('Verdana', 16))
    intro_label.grid(row=1, column=1, columnspan=3, sticky='NSEW')

    scrapeinfo_label_1 = Label(main_frame, bg='white', fg='black', text='Scrape latest car news from:')
    scrapeinfo_label_2 = Label(main_frame, bg='white', fg='black', text='Scrape car news by tags from:')
    scrapeinfo_label_3 = Label(main_frame, bg='white', fg='black', text='Scrape latest car news from:')

    scrapeinfo_label_1.configure(font=('Verdana', 12))
    scrapeinfo_label_2.configure(font=('Verdana', 12))
    scrapeinfo_label_3.configure(font=('Verdana', 12))

    scrapeinfo_label_1.grid(row=2, column=1, sticky='NSEW')
    scrapeinfo_label_2.grid(row=2, column=2, sticky='NSEW')
    scrapeinfo_label_3.grid(row=2, column=3, sticky='NSEW')

    autocar_scraper_button = Button(main_frame, text='autocar.co.uk', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_website(main_frame, scrape_autocar_articles))
    autoexpress_scraper_button = Button(main_frame, text='autoexpress.co.uk', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_website(main_frame, scrape_autoexpress_articles))
    caranddriver_scraper_button = Button(main_frame, text='caranddriver.com', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_website(main_frame, scrape_caranddriver_articles))
    motor1_scraper_button = Button(main_frame, text='motor1.com', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_website(main_frame, scrape_motor1_articles))
    topgear_scraper_button = Button(main_frame, text='topgear.com', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_website(main_frame, scrape_topgear_articles))

    autocar_google_button = Button(main_frame, text='autocar.co.uk', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_google_1(main_frame, scrape_autocar_articles_google))
    autoexpress_google_button = Button(main_frame, text='autoexpress.co.uk', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_google_1(main_frame, scrape_autoexpress_articles_google))
    caranddriver_google_button = Button(main_frame, text='caranddriver.com', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_google_1(main_frame, scrape_caranddriver_articles_google))
    motor1_google_button = Button(main_frame, text='motor1.com', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_google_1(main_frame, scrape_motor1_articles_google))
    topgear_google_button = Button(main_frame, text='topgear.com', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_google_1(main_frame, scrape_topgear_articles_google))

    autoweek_scraper_button = Button(main_frame, text='autoweek.com', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_website(main_frame, scrape_autoweek_articles))
    caradvice_scraper_button = Button(main_frame, text='caradvice.com.au', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_website(main_frame, scrape_caradvice_articles))
    motortrend_scraper_button = Button(main_frame, text='motortrend.com', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_website(main_frame, scrape_motortrend_articles))

    autocar_scraper_button.grid(row=3, column=1, sticky='NSEW', pady=10, padx=10)
    autoexpress_scraper_button.grid(row=4, column=1, sticky='NSEW', pady=10, padx=10)
    caranddriver_scraper_button.grid(row=5, column=1, sticky='NSEW', pady=10, padx=10)
    motor1_scraper_button.grid(row=6, column=1, sticky='NSEW', pady=10, padx=10)
    topgear_scraper_button.grid(row=7, column=1, sticky='NSEW', pady=10, padx=10)

    autocar_google_button.grid(row=3, column=2, sticky='NSEW', pady=10, padx=10)
    autoexpress_google_button.grid(row=4, column=2, sticky='NSEW', pady=10, padx=10)
    caranddriver_google_button.grid(row=5, column=2, sticky='NSEW', pady=10, padx=10)
    motor1_google_button.grid(row=6, column=2, sticky='NSEW', pady=10, padx=10)
    topgear_google_button.grid(row=7, column=2, sticky='NSEW', pady=10, padx=10)

    autoweek_scraper_button.grid(row=3, column=3, sticky='NSEW', pady=10, padx=10)
    caradvice_scraper_button.grid(row=4, column=3, sticky='NSEW', pady=10, padx=10)
    motortrend_scraper_button.grid(row=5, column=3, sticky='NSEW', pady=10, padx=10)

    exit_button = Button(main_frame, text='Quit', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=root.destroy)
    exit_button.grid(row=7, column=3, sticky='NSEW', pady=10, padx=10)

    root.mainloop()


def return_loading_frame(master):
    loading_frame = Frame(master, bg='white')
    loading_frame.grid_rowconfigure(0, weight=1)
    loading_frame.grid_columnconfigure(0, weight=1)
    loading_label = Label(loading_frame, bg='white', fg='black', text="Loading...")
    loading_label.configure(font=('Verdana', 16))
    loading_label.grid(row=0, column=0, sticky='NSEW')
    loading_label.update_idletasks()
    return loading_frame


def return_articles_frame(master_outer, articles_outer):
    articles_frame = Frame(master_outer, bg='white')

    articles_frame.grid_rowconfigure(0, weight=5)
    articles_frame.grid_rowconfigure(1, weight=2)
    articles_frame.grid_columnconfigure(0, weight=1)
    articles_frame.grid_columnconfigure(1, weight=1)

    def return_article_contents_frame(master_inner, articles_inner, article_idx):
        article_contents_frame_inner = Frame(master_inner, bg='white')

        article_contents_frame_inner.grid_rowconfigure(0, weight=1)
        article_contents_frame_inner.grid_rowconfigure(1, weight=1)
        article_contents_frame_inner.grid_rowconfigure(2, weight=1)
        article_contents_frame_inner.grid_rowconfigure(3, weight=10)
        article_contents_frame_inner.grid_columnconfigure(0, weight=1)

        article_title_label = Label(article_contents_frame_inner, text=articles_inner[article_idx]['article_title'], bg='white', fg='black')
        article_title_label.configure(font=('Verdana', 12))
        article_description_label = Label(article_contents_frame_inner, text=articles_inner[article_idx]['article_description'], bg='white', fg='black')
        article_description_label.configure(font=('Verdana', 12))
        article_date_label = Label(article_contents_frame_inner, text=articles_inner[article_idx]['article_date'], bg='white', fg='black')
        article_date_label.configure(font=('Verdana', 12))
        article_text = ScrolledText(article_contents_frame_inner, bg='white', fg='black', wrap=WORD, padx=20)
        article_text.configure(font=('Verdana', 10))
        article_text.insert(INSERT, articles_inner[article_idx]['article_contents'])
        article_text.configure(state=DISABLED)

        article_title_label.grid(row=0, column=0, sticky="NSEW")
        article_description_label.grid(row=1, column=0, sticky="NSEW")
        article_date_label.grid(row=2, column=0, sticky="NSEW")
        article_text.grid(row=3, column=0, sticky="NSEW")

        return article_contents_frame_inner

    current_article_idx = 0

    article_contents_frame_outer = return_article_contents_frame(articles_frame, articles_outer, current_article_idx)
    buttons_frame = Frame(articles_frame, bg='white')

    article_contents_frame_outer.grid(row=0, column=0, columnspan=2, sticky='NSEW')
    buttons_frame.grid(row=1, column=0, columnspan=2, sticky='NSEW')

    buttons_frame.rowconfigure(0, weight=1)
    buttons_frame.columnconfigure(0, weight=1)
    buttons_frame.columnconfigure(0, weight=1)

    def scroll_left():
        nonlocal current_article_idx
        nonlocal article_contents_frame_outer

        if not current_article_idx == 0:
            current_article_idx -= 1
            article_contents_frame_outer.destroy()
            article_contents_frame_outer = return_article_contents_frame(articles_frame, articles_outer, current_article_idx)
            article_contents_frame_outer.grid(row=0, column=0, columnspan=2, sticky='NSEW')

            if current_article_idx == 0:
                scroll_left_button['state'] = 'disabled'

            if current_article_idx < len(articles_outer) - 1:
                scroll_right_button['state'] = 'normal'

    def scroll_right():
        nonlocal current_article_idx
        nonlocal article_contents_frame_outer

        if not current_article_idx == len(articles_outer) - 1:
            current_article_idx += 1
            article_contents_frame_outer.destroy()
            article_contents_frame_outer = return_article_contents_frame(articles_frame, articles_outer, current_article_idx)
            article_contents_frame_outer.grid(row=0, column=0, columnspan=2, sticky='NSEW')

            if current_article_idx == len(articles_outer) - 1:
                scroll_right_button['state'] = 'disabled'

            if current_article_idx > 0:
                scroll_left_button['state'] = 'normal'

    scroll_left_button = Button(articles_frame, text='<--', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=scroll_left)
    scroll_right_button = Button(articles_frame, text='-->', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=scroll_right)

    scroll_left_button.grid(row=1, column=0, padx=10, pady=10, sticky='NSEW')
    scroll_right_button.grid(row=1, column=1, padx=10, pady=10, sticky='NSEW')

    scroll_left_button['state'] = 'disabled'

    return articles_frame


def scrape_website(master, website_scraper):
    top = Toplevel(master)
    top.geometry('1152x648')
    top.title('Scraping latest news')
    top.focus_set()

    top.grid_rowconfigure(0, weight=1)
    top.columnconfigure(0, weight=1)

    loading_frame = return_loading_frame(top)
    loading_frame.grid(row=0, column=0, sticky='NSEW')
    loading_frame.update_idletasks()

    articles = website_scraper()

    articles_frame = return_articles_frame(top, articles)
    loading_frame.destroy()
    articles_frame.grid(row=0, column=0, sticky='NSEW')
    articles_frame.update_idletasks()
    top.focus_set()


def return_tags_prompt_frame(master, previous_top, google_scraper):
    tags_prompt_frame = Frame(previous_top, bg='white')
    tags_prompt_frame.grid_rowconfigure(0, weight=1)
    tags_prompt_frame.grid_columnconfigure(0, weight=1)

    tags_prompt_inner_frame = Frame(tags_prompt_frame, bg='white')
    tags_prompt_inner_frame.grid_rowconfigure(0, weight=1)
    tags_prompt_inner_frame.grid_rowconfigure(1, weight=1)
    tags_prompt_inner_frame.grid_rowconfigure(2, weight=1)
    tags_prompt_inner_frame.columnconfigure(0, weight=1)

    tags_prompt_label = Label(tags_prompt_inner_frame, bg='white', fg='black', text='Please input search tags separated by space')
    tags_prompt_label.configure(font=('Verdana', 16))
    tags_prompt_entry = Entry(tags_prompt_inner_frame, bg='white', fg='black')
    tags_prompt_entry.configure(font=('Verdana', 16))
    tags_prompt_button = Button(tags_prompt_inner_frame, text='SEARCH', relief=RIDGE, bg='white', activebackground='black', activeforeground='white', command=lambda: scrape_google_2(master, previous_top, google_scraper, tags_prompt_entry.get().split(' ')))
    tags_prompt_button.configure(font=('Verdana', 16))

    tags_prompt_label.grid(row=0, column=0, sticky='NSEW', padx=50, pady=50)
    tags_prompt_entry.grid(row=1, column=0, sticky='NSEW', padx=50, pady=50)
    tags_prompt_button.grid(row=2, column=0, sticky='NSEW', padx=50, pady=50)

    tags_prompt_inner_frame.grid(row=0, column=0)

    return tags_prompt_frame


def scrape_google_1(master, google_scraper):
    top = Toplevel(master)
    top.geometry('1152x648')
    top.title('Scraping news by tags')
    top.focus_set()

    top.grid_rowconfigure(0, weight=1)
    top.columnconfigure(0, weight=1)

    tags_prompt_frame = return_tags_prompt_frame(master, top, google_scraper)
    tags_prompt_frame.grid(row=0, column=0, sticky='NSEW')


def scrape_google_2(master, previous_top, google_scraper, tags):
    previous_top.destroy()

    top = Toplevel(master)
    top.geometry('1152x648')
    top.title('Scraping news by tags')
    top.focus_set()

    top.grid_rowconfigure(0, weight=1)
    top.columnconfigure(0, weight=1)

    loading_frame = return_loading_frame(top)
    loading_frame.grid(row=0, column=0, sticky='NSEW')
    loading_frame.update_idletasks()

    articles = google_scraper(tags)

    if articles:
        articles_frame = return_articles_frame(top, articles)
        loading_frame.destroy()
        articles_frame.grid(row=0, column=0, sticky='NSEW')
        articles_frame.update_idletasks()
        top.focus_set()
    else:
        no_articles_frame = Frame(top, bg='white')
        no_articles_frame.grid_rowconfigure(0, weight=1)
        no_articles_frame.grid_columnconfigure(0, weight=1)
        no_articles_label = Label(no_articles_frame, bg='white', fg='black', text='No articles found for given tags :(')
        no_articles_label.configure(font=('Verdana', 16))
        no_articles_label.grid(row=0, column=0, sticky='NSEW')

        loading_frame.destroy()
        no_articles_frame.grid(row=0, column=0, sticky='NSEW')
        no_articles_frame.update_idletasks()
        top.focus_set()
