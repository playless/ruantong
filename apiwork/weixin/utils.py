import logging

logging.basicConfig(level=logging.DEBUG)


def parse_content(content, kwargs):
    if isinstance(content, dict):
        logging.debug({
            key: parse_content(value, kwargs)
            for key, value in content.items()
        })
        return {
            key: parse_content(value, kwargs)
            for key, value in content.items()
        }

    elif isinstance(content, list):
        logging.debug([
            parse_content(item, kwargs)
            for item in content
        ])
        return [
            parse_content(item, kwargs)
            for item in content
        ]

    elif isinstance(content, str):
        logging.debug(content.format(**kwargs))
        return content.format(**kwargs)

    else:
        logging.debug(content)
        return content
