import os
from bs4 import BeautifulSoup

def clean_bbc():
    input_path = '/home/ubuntuvm/Projects/demo/Task3/bbc_raw.html'
    output_path = '/home/ubuntuvm/Projects/demo/Task3/index.html'
    
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. REMOVE UNNECESSARY ELEMENTS
    for element in soup.find_all(['script', 'noscript', 'button', 'aside', 'form', 'footer']):
        element.decompose()
        
    for ad in soup.find_all('div', {'data-component': 'ad-slot'}):
        ad.decompose()
        
    for skip in soup.find_all('a', {'href': '#bbc-main'}):
        skip.decompose()
        
    for a in soup.find_all('a'):
        a['href'] = '#'
        
    # 2. FIND THE MAIN ARTICLE
    article = soup.find('article')
    if not article:
        print("Error: Could not find <article> tag.")
        return
        
    # Extract structural classes from existing elements before clearing
    h1_tag = article.find('h1')
    h1_class = " ".join(h1_tag.get('class', [])) if h1_tag else "fiwhPQ"
    
    p_example = article.find('p')
    p_class = " ".join(p_example.get('class', [])) if p_example else "HooNV"

    # Standard BBC classes for subheadings (found in raw HTML)
    h2_class = "dkPqjG" # 24px Serif
    h3_class = "eQumHa" # 18px Serif
    meta_class = "fXmcMt" # 12px Sans
    
    # Clear article contents
    article.clear()
    
    # 3. CONSTRUCT NEW CONTENT
    new_content = f'''
    <div data-component="headline-block" class="sc-9cd5bb24-0 cmjZrf">
        <div class="sc-cd6075cf-0 DQtHs">
            <div class="sc-82b3c53b-0 gmICnp">
                <h1 class="{h1_class}">Майбутнє розумних будинків: як ШІ змінює наш побут</h1>
                <p class="{meta_class}" style="margin-top: 10px; color: #545658; font-family: 'BBC Reith Sans',Arial,sans-serif;">15 квітня 2026 • Технології</p>
            </div>
        </div>
    </div>
    
    <div data-component="image-block" class="sc-9cd5bb24-0 jTWPCV">
        <figure class="sc-cd6075cf-0 laOREU">
            <div class="sc-82b3c53b-0 ciXMDU">
                <img src="img1.png" alt="Розкішний розумний дім" style="width:100%; height:auto; border-radius:4px;">
            </div>
        </figure>
    </div>

    <div data-component="text-block" class="sc-9cd5bb24-0 lmzibM">
        <div class="sc-cd6075cf-0 DQtHs">
            <div class="sc-82b3c53b-0 IAFLu">
                <p class="{p_class}">Штучний інтелект стає не просто доповненням, а серцем сучасного житла. Завдяки новим алгоритмам обробки даних, наші будинки починають "розумнішати" не щодня, а щогодини. За даними <a href="#" style="color: rgb(32, 34, 36); font-family: BBC Reith Serif, BBCReithSerif-fallback, serif; font-weight: 500; font-size: 18px; line-height: 26px; text-transform: none; text-decoration: underline; letter-spacing: -0.36px;">Reuters Technology</a>, попит на домашню автоматизацію зріс рекордними темпами.</p>
                <p class="{p_class}">Системи аналізують поведінкові сценарії: коли мешканці прокидаються, як часто користуються побутовою технікою, які кімнати найактивніші в різні години. На основі цього автоматично формується комфортний режим освітлення, температури, вентиляції та безпеки без ручного втручання.</p>
            </div>
        </div>
    </div>

    <div data-component="text-block" class="sc-9cd5bb24-0 lmzibM">
        <div class="sc-cd6075cf-0 DQtHs">
            <div class="sc-82b3c53b-0 IAFLu">
                <h2 class="{h2_class}" style="margin: 32px 0 16px;">Революція в управлінні</h2>
                <p class="{p_class}">Сучасні системи більше не потребують ручного налаштування. Вони самостійно регулюють рівень освітлення залежно від часу доби та вашого настрою, а також оптимізують енергоспоживання в реальному часі.</p>
                <p class="{p_class}">Ключова зміна — перехід від реактивного до проактивного управління. Дім не просто виконує команди, а передбачає потреби: готує робочу зону до онлайн-зустрічі, вмикає режим тиші для сну дітей, знижує навантаження на мережу у пікові години та попереджає про потенційні збої обладнання.</p>
                <p class="{p_class}">За оцінками ринку, найбільше впровадження спостерігається в новобудовах бізнес-класу, але за останні роки такі рішення стали доступними і для звичайних квартир. Модульна архітектура дозволяє починати з базових датчиків та поступово масштабувати систему до повноцінної екосистеми «розумного дому». Детальніше про підходи до масштабування описано у <a href="#" style="color: rgb(32, 34, 36); font-family: BBC Reith Serif, BBCReithSerif-fallback, serif; font-weight: 500; font-size: 18px; line-height: 26px; text-transform: none; text-decoration: underline; letter-spacing: -0.36px;">BBC Future</a>.</p>
            </div>
        </div>
    </div>

    <div data-component="image-block" class="sc-9cd5bb24-0 jTWPCV">
        <figure class="sc-cd6075cf-0 laOREU">
            <div class="sc-82b3c53b-0 ciXMDU">
                <img src="img2.png" alt="Інтерфейс безпеки" style="width:100%; height:auto; border-radius:4px;">
            </div>
        </figure>
    </div>

    <div data-component="text-block" class="sc-9cd5bb24-0 lmzibM">
        <div class="sc-cd6075cf-0 DQtHs">
            <div class="sc-82b3c53b-0 IAFLu">
                <h3 class="{h3_class}" style="margin: 24px 0 12px;">Основні переваги ШІ-дому:</h3>
                <ul class="{p_class}" style="list-style: disc; padding-left: 24px; margin-bottom: 24px;">
                    <li style="margin-bottom: 12px;"><strong>Голосове управління:</strong> Природне спілкування з будинком як з живим асистентом.</li>
                    <li style="margin-bottom: 12px;"><strong>Превентивна безпека:</strong> Розпізнавання небезпечних ситуацій ще до їхнього виникнення.</li>
                    <li style="margin-bottom: 12px;"><strong>Максимальна енергоефективність:</strong> Зменшення витрат на опалення та світло до 40%.</li>
                    <li style="margin-bottom: 12px;"><strong>Гнучка інтеграція:</strong> Підключення камер, замків, клімат-контролю та мультимедіа в єдину систему.</li>
                    <li style="margin-bottom: 12px;"><strong>Аналітика для рішень:</strong> Детальні звіти про витрати ресурсів і поведінкові патерни мешканців.</li>
                </ul>
                <p class="{p_class}">Окрему увагу девелопери приділяють кібербезпеці. Нові пристрої мають шифрування каналів зв'язку, двофакторну авторизацію, контроль доступу для кожного члена родини та журнал дій. Це особливо важливо, коли до системи підключені відеоспостереження, електронні замки та платіжні сервіси. Ринкові кейси регулярно публікує <a href="#" style="color: rgb(32, 34, 36); font-family: BBC Reith Serif, BBCReithSerif-fallback, serif; font-weight: 500; font-size: 18px; line-height: 26px; text-transform: none; text-decoration: underline; letter-spacing: -0.36px;">Reuters Digital Homes</a>.</p>
            </div>
        </div>
    </div>

    <div data-component="image-block" class="sc-9cd5bb24-0 jTWPCV">
        <figure class="sc-cd6075cf-0 laOREU">
            <div class="sc-82b3c53b-0 ciXMDU">
                <img src="img3.png" alt="Голосовий асистент" style="width:100%; height:auto; border-radius:4px;">
            </div>
        </figure>
    </div>

    <div data-component="text-block" class="sc-9cd5bb24-0 lmzibM">
        <div class="sc-cd6075cf-0 DQtHs">
            <div class="sc-82b3c53b-0 IAFLu">
                <p class="{p_class}">Майбутнє вже тут. Питання лише в тому, наскільки швидко ми готові довірити свій побут цифровим помічникам, які знають про нас більше, ніж ми самі.</p>
                <p class="{p_class}">Наступний етап розвитку — персоналізовані моделі ШІ для кожного дому: вони враховуватимуть не лише розклад, а й стан здоров'я, рівень стресу, сезонні звички та навіть якість сну. У підсумку «розумний дім» поступово перетворюється на платформу, що підтримує комфорт, безпеку та енергоефективність як єдину систему.</p>
            </div>
        </div>
    </div>
    '''
    
    article.append(BeautifulSoup(new_content, 'html.parser'))
    
    title_tag = soup.find('title')
    if title_tag:
        title_tag.string = "Майбутнє розумних будинків — BBC News"
        
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Successfully generated {output_path}")

if __name__ == '__main__':
    clean_bbc()
