from milligram import Telegram


def test_get_me_success(requests_mock):
    url = f'https://api.telegram.org/bot123:xyz/getMe'
    token = '123:xyz'
    data = {'ok': True,
            'result': {'id': 196935790,
                       'is_bot': True,
                       'first_name': 'test',
                       'username': 'testbot',
                       'can_join_groups': True,
                       'can_read_all_group_messages': False,
                       'supports_inline_queries': False}
            }

    requests_mock.post(url, json=data)
    telegram = Telegram(token)
    response = telegram.get_me()
    assert response == data
