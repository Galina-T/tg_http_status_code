import os

token = os.environ.get('BOT_TOKEN')

current_menu_msg = (f"<b>Напиши свой статус код.</b>"
                    f"\n<b><i>Или выбери из списка</i></b>👇🏻")

back_to_menu_msg = (f"<b>Напиши свой статус код.</b>"
                    f"\n<b><i>Или выбери команду</i></b>👇🏻")

incorrect_format_msg = (f"🧐<b>Я не понимаю тебя.</b>\n\n"
                        f"<b>Напиши статус код</b>\n"
                        f"<b><i>Или выбери команду</i></b>👇🏻")

status_code_is_none_msg = (f"🤔 Такого кода ответа (состояния), нет в моем списке...\n"
                           f"💡 Возможно он является не стандартизированным и вероятней всего он кастомный сервера.")

btn_back_to_main_menu_text = "↩️ В главное меню"

btns_for_status_code_response = {
    "mdn": "👀 Веб-документация MDN.",
    "dev": "⭐ А здесь подробнее и с примерами."
}

status_code_types =[
    {
        "title": "Информационные",
        "description": (f"В этом диапазоне возвращаются коды, которые информируют о процессе передачи данных.\n"
                        f"В версии HTTP 1.0 их следует игнорировать.\n"
                        f"В версии HTTP 1.1 этот класс сообщений принимают как обычный ответ, но отправлять серверу ничего не нужно."),
        "icon": "ℹ️",
        "note": "1xx",
        "img": "./img/informational.png"
    }, {
        "title": "Успешные",
        "description": "Коды в этом диапазоне сообщают, что запрос клиента получен, понят и принят.",
        "icon": "✅",
        "note": "2xx",
        "img": "./img/successful.png"
    }, {
        "title": "Редиректы",
        "description": (f"Коды в этом диапазоне сообщают, что для успешного выполнения действия необходимо сделать другой запрос.\n"
                        f"Как правило, достаточно изменить URL.\n"
                        f"Перенаправление может выполняться и без запроса пользователя, если второй ресурс запрашивается методом GET или HEAD."),
        "icon": "👣",
        "note": "3xx",
        "img": "./img/redirection.png"
    }, {
        "title": "Клиентские ошибки",
        "description": (f"Сервер не обработал запрос из-за синтаксической ошибки.\n"
                        f"Например, не хватает данных или есть проблемы с валидацией домена.\n"
                        f"Клиенту не следует повторять запрос без изменений, так как это снова приведет к появлению ошибки 400."),
        "icon": "⚠️",
        "note": "4xx",
        "img": "./img/client_error.png"
    }, {
        "title": "Серверные ошибки",
        "description": (f"Коды из этого диапазона возвращаются в случаях, когда сервер знает, что "
                        f"произошла ошибка или не может обработать запрос.\n"
                        f"При использовании всех методов, кроме HEAD, в теле ответа указывается объяснение ошибки."),
        "icon": "❗",
        "note": "5xx",
        "img": "./img/server_error.png"
    }
]

status_codes = {
    "100": {
      "type": "Информационные",
      "name": "Continue/Продолжить",
      "description": "Является одним из информационных HTTP-ответов, возвращаемых сервером.\nЭто указывает на то, что сеанс HTTP проходит, как и ожидалось, и просит клиента перейти к следующему шагу.\nКлиент может безопасно игнорировать этот HTTP-ответ, если HTTP-запрос завершен.\nОтвет HTTP отправляется только тогда, когда клиент включает поле запроса HTTP-заголовка Expect.",
      "version": "HTTP/1.1",
      "img": "./img/100.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/100",
          "dev": "https://http.dev/100"
      }
    },
    "101": {
      "type": "Информационные",
      "name": "Switching Protocol/Переключение протокола",
      "description": "Этот код присылается в ответ на запрос клиента, содержащий заголовок <code>Upgrade:</code>, и указывает, что сервер переключился на протокол, который был указан в заголовке.\nЭта возможность позволяет перейти на несовместимую версию протокола и обычно не используется.",
      "version": "HTTP/1.1",
      "img": "./img/101.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/101",
          "dev": "https://http.dev/101"
      }
    },
    "102": {
      "type": "Информационные",
      "name": "Processing/В обработке",
      "description": "Этот код указывает, что сервер получил запрос и обрабатывает его, но обработка ещё не завершена.",
      "version": "HTTP/1.1",
      "img": "./img/102.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/102",
          "dev": "https://http.dev/102"
      }
    },
    "103": {
      "type": "Информационные",
      "name": "Early Hints/Ранние подсказки",
      "description": "В ответе сообщаются ресурсы, которые могут быть загружены заранее, пока сервер будет подготавливать основной ответ. <a href='https://datatracker.ietf.org/doc/rfc8297'>RFC 8297 (Experimental)</a>.",
      "version": "HTTP/1.1",
      "img": "./img/103.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/103",
          "dev": "https://http.dev/103"
      }
    },
    "200": {
      "type": "Успешные",
      "name": "OK/Успешно",
      "description": "Запрос успешно обработан.\nЧто значит 'успешно', зависит от метода HTTP, который был запрошен:\n &#8226; GET: 'ПОЛУЧИТЬ'. Запрошенный ресурс был найден и передан в теле ответа.\n &#8226; HEAD: 'ЗАГОЛОВОК'. Заголовки переданы в ответе.\n &#8226; POST: 'ПОСЫЛКА'. Ресурс, описывающий результат действия сервера на запрос, передан в теле ответа.\n &#8226; TRACE: 'ОТСЛЕЖИВАТЬ'. Тело ответа содержит тело запроса полученного сервером.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/200.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/200",
          "dev": "https://http.dev/200"
      }
    },
    "201": {
      "type": "Успешные",
      "name": "Created/Создано",
      "description": "Запрос успешно выполнен и в результате был создан ресурс.\nЭтот код обычно присылается в ответ на запрос POST или PUT.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/201.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/201",
          "dev": "https://http.dev/201"
      }
    },
    "202": {
      "type": "Успешные",
      "name": "Accepted/Принято",
      "description": "Запрос принят, но ещё не обработан.\nНе поддерживаемо, т.е., нет способа с помощью HTTP отправить асинхронный ответ позже, который будет показывать итог обработки запроса.\nЭто предназначено для случаев, когда запрос обрабатывается другим процессом или сервером, либо для пакетной обработки.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/202.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/202",
          "dev": "https://http.dev/202"
      }
    },
    "203": {
      "type": "Успешные",
      "name": "Non-Authoritative Information/Информация не авторитетна",
      "description": "Этот код ответа означает, что информация, которая возвращена, была предоставлена не от исходного сервера, а из какого-нибудь другого источника.\nНапример, это данные из кеша или резервной копии, которые могли устареть.\nВо всех остальных ситуациях более предпочтителен код ответа 200 OK.",
      "version": "HTTP/0.9 и 1.1",
      "img": "./img/203.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/203",
          "dev": "https://http.dev/203"
      }
    },
    "204": {
      "type": "Успешные",
      "name": "No Content/Нет содержимого",
      "description": "Нет содержимого для ответа на запрос, но заголовки ответа, которые могут быть полезны, присылаются.\nКлиент может использовать их для обновления кешированных заголовков полученных ранее для этого ресурса.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/204.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/204",
          "dev": "https://http.dev/204"
      }
    },
    "205": {
      "type": "Успешные",
      "name": "Reset Content/Сбросить содержимое",
      "description": "Этот код присылается, когда запрос обработан, чтобы сообщить клиенту, что необходимо сбросить отображение документа, который прислал этот запрос.",
      "version": "HTTP/1.1",
      "img": "./img/205.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/205",
          "dev": "https://http.dev/205"
      }
    },
    "206": {
      "type": "Успешные",
      "name": "Partial Content/Частичное содержимое",
      "description": "Этот код ответа используется, когда клиент присылает заголовок диапазона, чтобы выполнить загрузку отдельно, в несколько потоков.",
      "version": "HTTP/1.1",
      "img": "./img/206.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/206",
          "dev": "https://http.dev/206"
      }
    },
    "207": {
      "type": "Успешные",
      "name": "Multi-Status/Мультистатус",
      "description": "Сервер передает результаты выполнения нескольких операций.\nВозможность возврата набора ресурсов является частью протокола WebDAV (ее могут получать веб-приложения, обращающиеся к серверу WebDAV).\nБраузеры, обращающиеся к веб-страницам, никогда не обнаружат этот код состояния.",
      "version": "RFC 4918",
      "img": "./img/207.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/207",
          "dev": "https://http.dev/207"
      }
    },
    "226": {
      "type": "Успешные",
      "name": "IM Used/",
      "description": "Сервер принял заголовок A-IM и возвращает содержимое, учитывая параметры.",
      "version": "HTTP/1.1",
      "img": "./img/226.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/226",
          "dev": "https://http.dev/226"
      }
    },
    "300": {
      "type": "Редиректы",
      "name": "Multiple Choice/Множественный выбор",
      "description": "Этот код ответа присылается, когда запрос имеет более чем один из возможных ответов.\nИ User-agent или пользователь должен выбрать один из ответов.\nНе существует стандартизированного способа выбора одного из полученных ответов.",
      "version": "HTTP/1.0 и выше",
      "img": "./img/300.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/300",
          "dev": "https://http.dev/300"
      }
    },
    "301": {
      "type": "Редиректы",
      "name": "Moved Permanently/Перемещён на постоянной основе",
      "description": "Этот код ответа значит, что URL запрашиваемого ресурса был изменён.\nВозможно, новый URL будет предоставлен в ответе.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/301.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/301",
          "dev": "https://http.dev/301"
      }
    },
    "302": {
      "type": "Редиректы",
      "name": "Found/Найдено",
      "description": "Этот код ответа значит, что запрошенный ресурс <em>временно изменён</em>.\nНовые изменения в URL могут быть доступны в будущем.\nТаким образом, этот URL, должен быть использован клиентом в будущих запросах.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/302.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/302",
          "dev": "https://http.dev/302"
      }
    },
    "303": {
      "type": "Редиректы",
      "name": "See Other/Просмотр других ресурсов",
      "description": "Этот код ответа присылается, чтобы направлять клиента для получения запрашиваемого ресурса в другой URL с запросом GET.",
      "version": "HTTP/0.9 и 1.1",
      "img": "./img/303.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/303",
          "dev": "https://http.dev/303"
      }
    },
    "304": {
      "type": "Редиректы",
      "name": "Not Modified/Не модифицировано",
      "description": "Используется для кеширования.\nЭто код ответа значит, что запрошенный ресурс не был изменён.\nТаким образом, клиент может продолжать использовать кешированную версию ответа.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/304.png",
      "links": {
          "mdn": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/304",
          "dev": "https://http.dev/304"
      }
    },
    "305": {
      "type": "Редиректы",
      "name": "Use Proxy/Использовать прокси",
      "description": "Определено в предыдущей версии спецификации HTTP, чтобы указать, что запрошенный ответ должен быть доступен через прокси.\n\nОн <u>устарел</u> из-за проблем безопасности, связанных с внутренней конфигурацией прокси-сервера.",
      "version": "HTTP/1.1",
      "img": "./img/305.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status",
          "dev": "https://http.dev/305"
      }
    },
    "306": {
      "type": "Редиректы",
      "name": "Switch Proxy/",
      "description": "Больше <u>не используется</u>.\nИзначально подразумевалось, что 'последующие запросы должны использовать указанный прокси.'",
      "version": "HTTP/1.1",
      "img": "./img/306.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status",
          "dev": "https://http.dev/306"
      }
    },
    "307": {
      "type": "Редиректы",
      "name": "Temporary Redirect/Временное перенаправление",
      "description": "Сервер отправил этот ответ, чтобы клиент получил запрошенный ресурс на другой URL-адрес с тем же методом, который использовал предыдущий запрос.\nДанный код имеет ту же семантику, что код ответа <code>302 Found</code>, за исключением того, что агент пользователя не должен изменять используемый метод HTTP: если в первом запросе использовался <code>POST</code>, то во втором запросе также должен использоваться <code>POST</code>.",
      "version": "HTTP/1.1",
      "img": "./img/307.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/307",
          "dev": "https://http.dev/307"
      }
    },
    "308": {
      "type": "Редиректы",
      "name": "Permanent Redirect/Перенаправление на постоянной основе",
      "description": "Это означает, что ресурс теперь постоянно находится в другом URL, указанном в заголовке <code>Location:</code> HTTP Response.\nДанный код ответа имеет ту же семантику, что и код ответа <code>301 Moved Permanently</code>, за исключением того, что агент пользователя не должен изменять используемый метод HTTP: если <code>POST</code> использовался в первом запросе, <code>POST</code> должен использоваться и во втором запросе.\n<strong>Примечание:</strong> Это экспериментальный код ответа, Спецификация которого в настоящее время находится в черновом виде.",
      "version": "Черновик спецификации",
      "img": "./img/308.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/308",
          "dev": "https://http.dev/308"
      }
    },
    "400": {
      "type": "Клиентские ошибки",
      "name": "Bad Request/Плохой запрос",
      "description": "Этот ответ означает, что сервер не понимает запрос из-за неверного синтаксиса.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/400.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400",
          "dev": "https://http.dev/400"
      }
    },
    "401": {
      "type": "Клиентские ошибки",
      "name": "Unauthorized/Неавторизованно",
      "description": "Для получения запрашиваемого ответа нужна аутентификация.\nСтатус похож на статус 403, но,в этом случае, аутентификация возможна.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/401.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401",
          "dev": "https://http.dev/401"
      }
    },
    "402": {
      "type": "Клиентские ошибки",
      "name": "Payment Required/Необходима оплата",
      "description": "Этот код ответа зарезервирован для будущего использования.\nПервоначальная цель для создания этого кода была в использовании его для цифровых платёжных систем(на данный момент не используется).",
      "version": "HTTP/0.9 и 1.1",
      "img": "./img/402.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/402",
          "dev": "https://http.dev/402"
      }
    },
    "403": {
      "type": "Клиентские ошибки",
      "name": "Forbidden/Запрещено",
      "description": "У клиента нет прав доступа к содержимому, поэтому сервер отказывается дать надлежащий ответ.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/403.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403",
          "dev": "https://http.dev/403"
      }
    },
    "404": {
      "type": "Клиентские ошибки",
      "name": "Not Found/Не найден",
      "description": "Сервер не может найти запрашиваемый ресурс.\nКод этого ответа, наверно, самый известный из-за частоты его появления в вебе.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/404.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404",
          "dev": "https://http.dev/404"
      }
    },
    "405": {
      "type": "Клиентские ошибки",
      "name": "Method Not Allowed/Метод не разрешён",
      "description": "Сервер знает о запрашиваемом методе, но он был деактивирован и не может быть использован.\nДва обязательных метода, <code>GET</code> и <code>HEAD</code>, никогда не должны быть деактивированы и не должны возвращать этот код ошибки.",
      "version": "HTTP/1.1",
      "img": "./img/405.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/405",
          "dev": "https://http.dev/405"
      }
    },
    "406": {
      "type": "Клиентские ошибки",
      "name": "Not Acceptable/",
      "description": "Этот ответ отсылается, когда веб сервер после выполнения <a href='/en-US/HTTP/Content_negotiation#server-driven_negotiation'>server-driven content negotiation</a>, не нашёл контента, отвечающего критериям, полученным из user agent.",
      "version": "HTTP/1.1",
      "img": "./img/406.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/406",
          "dev": "https://http.dev/406"
      }
    },
    "407": {
      "type": "Клиентские ошибки",
      "name": "Proxy Authentication Required/",
      "description": "Этот код ответа аналогичен коду 401, только аутентификация требуется для прокси сервера.",
      "version": "HTTP/1.1",
      "img": "./img/407.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/407",
          "dev": "https://http.dev/407"
      }
    },
    "408": {
      "type": "Клиентские ошибки",
      "name": "Request Timeout/",
      "description": "Ответ с таким кодом может прийти, даже без предшествующего запроса.\nОн означает, что сервер хотел бы отключить это неиспользуемое соединение.\nЭтот метод используется все чаще с тех пор, как некоторые браузеры, вроде Chrome и IE9, стали использовать <a href='http://www.belshe.com/2011/02/10/the-era-of-browser-preconnect/'>HTTP механизмы предварительного соединения</a> для ускорения сёрфинга (смотрите <a href='https://bugzilla.mozilla.org/show_bug.cgi?id=634278'>баг&nbsp;634278</a>, будущей реализации этого механизма в Firefox).\nТакже учитывайте, что некоторые серверы прерывают соединения не отправляя подобных сообщений.",
      "version": "HTTP/1.1",
      "img": "./img/408.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408",
          "dev": "https://http.dev/408"
      }
    },
    "409": {
      "type": "Клиентские ошибки",
      "name": "Conflict/",
      "description": "Этот ответ отсылается, когда запрос конфликтует с текущим состоянием сервера.",
      "version": "HTTP/1.1",
      "img": "./img/409.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409",
          "dev": "https://http.dev/409"
      }
    },
    "410": {
      "type": "Клиентские ошибки",
      "name": "Gone/",
      "description": "Этот ответ отсылается, когда запрашиваемый контент удалён с сервера.",
      "version": "HTTP/1.1",
      "img": "./img/410.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/410",
          "dev": "https://http.dev/410"
      }
    },
    "411": {
      "type": "Клиентские ошибки",
      "name": "Length Required/",
      "description": "Запрос отклонён, потому что сервер требует указание заголовка <code>Content-Length</code>, но он не указан.",
      "version": "HTTP/1.1",
      "img": "./img/411.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/411",
          "dev": "https://http.dev/411"
      }
    },
    "412": {
      "type": "Клиентские ошибки",
      "name": "Precondition Failed/",
      "description": "Клиент указал в своих заголовках условия, которые сервер не может выполнить.",
      "version": "HTTP/1.1",
      "img": "./img/412.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/412",
          "dev": "https://http.dev/412"
      }
    },
    "413": {
      "type": "Клиентские ошибки",
      "name": "Request Entity Too Large/",
      "description": "Размер запроса превышает лимит, объявленный сервером.\nСервер может закрыть соединение, вернув заголовок <code>Retry-After</code>",
      "version": "HTTP/1.1",
      "img": "./img/413.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/413",
          "dev": "https://http.dev/413"
      }
    },
    "414": {
      "type": "Клиентские ошибки",
      "name": "Request-URL Too Long/",
      "description": "URL запрашиваемый клиентом слишком длинный для того, чтобы сервер смог его обработать",
      "version": "HTTP/1.1",
      "img": "./img/414.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/414",
          "dev": "https://http.dev/414"
      }
    },
    "415": {
      "type": "Клиентские ошибки",
      "name": "Unsupported Media Type/",
      "description": "Медиа формат запрашиваемых данных не поддерживается сервером, поэтому запрос отклонён",
      "version": "HTTP/1.1",
      "img": "./img/415.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/415",
          "dev": "https://http.dev/415"
      }
    },
    "416": {
      "type": "Клиентские ошибки",
      "name": "Requested Range Not Satisfiable/",
      "description": "Диапазон указанный заголовком запроса <code>Range</code> не может быть выполнен.\nВозможно, он выходит за пределы переданного URL",
      "version": "HTTP/1.1",
      "img": "./img/416.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/416",
          "dev": "https://http.dev/416"
      }
    },
    "417": {
      "type": "Клиентские ошибки",
      "name": "Expectation Failed",
      "description": "Этот код ответа означает, что ожидание, полученное из заголовка запроса <code>Expect</code>, не может быть выполнено сервером.",
      "version": "HTTP/1.1",
      "img": "./img/417.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/417",
          "dev": "https://http.dev/417"
      }
    },
    "418": {
      "type": "Клиентские ошибки",
      "name": "I’m a teapot",
      "description": "Код появился 1 апреля 1998 года как шутка.\nОжидалось, что он не будет поддерживаться реальными серверами.\nОднако реализация кода состояния 418 существует.\nНапример, Nginx использует его для имитации goto-подобного поведения.",
      "version": "RFC 2324",
      "img": "./img/418.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418",
          "dev": "https://http.dev/418"
      }
    },
    "422": {
      "type": "Клиентские ошибки",
      "name": "Unprocessable Entity (WebDAV)",
      "description": "Сервер возвращает этот код, если синтаксически запрос был правильным, указанный вид данных поддерживается, но выполнить инструкции невозможно.\nНапример, это может быть связано с семантическими ошибками.",
      "version": "RFC 4918",
      "img": "./img/422.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422",
          "dev": "https://http.dev/422"
      }
    },
    "423": {
      "type": "Клиентские ошибки",
      "name": "Locked (WebDAV)",
      "description": "Статус говорит о том, что целевой ресурс недоступен для указанного метода.\nВ ответе должно содержаться предусловие или постусловие, например, ‘lock-token-submitted’ или ‘no-conflicting-lock’.",
      "version": "RFC 4918",
      "img": "./img/423.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/423",
          "dev": "https://http.dev/423"
      }
    },
    "426": {
      "type": "Клиентские ошибки",
      "name": "Upgrade Required",
      "description": "Вместе с кодом 426 сервер отправляет, какие именно расширения используются для доступа к ресурсу.\nКлиент должен выбрать подходящий протокол",
      "version": "RFC 7231",
      "img": "./img/426.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/426",
          "dev": "https://http.dev/426"
      }
    },
    "429": {
      "type": "Клиентские ошибки",
      "name": "Too Many Requests",
      "description": "Пользователь отправил слишком много запросов в указанный промежуток времени.\nВ ответе должна быть информация об ограничениях.\nПри этом серверы не обязаны использовать код 429, так как каждый ответ потребляет ресурсы.\nВместо возвращения ошибки можно, например, разрывать соединение.",
      "version": "RFC 6585",
      "img": "./img/429.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429",
          "dev": "https://http.dev/429"
      }
    },
    "500": {
      "type": "Серверные ошибки",
      "name": "Internal Server Error/Внутренняя ошибка сервера",
      "description": "Сервер столкнулся с ситуацией, которую он не знает как обработать.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/500.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500",
          "dev": "https://http.dev/500"
      }
    },
    "501": {
      "type": "Серверные ошибки",
      "name": "Not Implemented/Не реализовано",
      "description": "Метод запроса не поддерживается сервером и не может быть обработан.\nЕдинственные методы, которые сервера должны поддерживать (и, соответственно, не должны возвращать этот код) - <code>GET</code> и <code>HEAD</code>.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/501.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/501",
          "dev": "https://http.dev/501"
      }
    },
    "502": {
      "type": "Серверные ошибки",
      "name": "Bad Gateway/Плохой шлюз",
      "description": "Эта ошибка означает что сервер, во время работы в качестве шлюза для получения ответа, нужного для обработки запроса, получил недействительный (недопустимый) ответ.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/502.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502",
          "dev": "https://http.dev/502"
      }
    },
    "503": {
      "type": "Серверные ошибки",
      "name": "Service Unavailable/Сервис недоступен",
      "description": "Сервер не готов обрабатывать запрос.\nЗачастую причинами являются отключение сервера или то, что он перегружен.\nОбратите внимание, что вместе с этим ответом удобная для пользователей(user-friendly) страница должна отправлять объяснение проблемы.\nЭтот ответ должен использоваться для временных условий и <code>Retry-After:</code> HTTP-заголовок должен, если возможно, содержать предполагаемое время до восстановления сервиса.\nВеб-мастер также должен позаботиться о заголовках, связанных с кешем, которые отправляются вместе с этим ответом, так как эти ответы, связанные с временными условиями, обычно не должны кешироваться.",
      "version": "HTTP/0.9 и выше",
      "img": "./img/503.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503",
          "dev": "https://http.dev/503"
      }
    },
    "504": {
      "type": "Серверные ошибки",
      "name": "Gateway Timeout/",
      "description": "Этот ответ об ошибке предоставляется, когда сервер действует как шлюз и не может получить ответ вовремя.",
      "version": "HTTP/1.1",
      "img": "./img/504.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504",
          "dev": "https://http.dev/504"
      }
    },
    "505": {
      "type": "Серверные ошибки",
      "name": "HTTP Version Not Supported/HTTP-версия не поддерживается",
      "description": "HTTP-версия, используемая в запросе, не поддерживается сервером.",
      "version": "HTTP/1.1",
      "img": "./img/505.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/505",
          "dev": "https://http.dev/505"
      }
    },
    "507": {
      "type": "Серверные ошибки",
      "name": "Insufficient Storage (WebDAV)",
      "description": "Нет места для успешного выполнения запроса, некуда сохранить представление.",
      "version": "RFC 4918",
      "img": "./img/507.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/507",
          "dev": "https://http.dev/507"
      }
    },
    "509": {
      "type": "Серверные ошибки",
      "name": "Bandwidth Limit Exceeded (Apache)",
      "description": "Веб-площадка превысила лимит на потребление трафика.\nВведен панелью управления хостингом cPanel, используется ей.",
      "version": "Только cPanel",
      "img": "./img/509.png",
      "links": {
          "dev": "https://http.dev/509"
      }
    },
    "510": {
      "type": "Серверные ошибки",
      "name": "Not Extended",
      "description": "Не соблюдена политика доступа.\nСервер в ответ должен прислать информацию, которая поможет клиенту отправить расширенный запрос.",
      "version": "RFC 2774",
      "img": "./img/510.png",
      "links": {
          "mdn": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/510",
          "dev": "https://http.dev/510"
      }
    },
}
