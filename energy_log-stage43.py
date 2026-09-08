# === Stage 43: Добавь пагинацию длинных списков ===
# Project: EnergyLog
def paginate(items, page_size=10):
    """Paginate a list of items into chunks of page_size.

    Args:
        items: Iterable of items to paginate.
        page_size: Number of items per page.

    Returns:
        List of pages, where each page is a list of items.
    """
    pages = []
    for i in range(0, len(items), page_size):
        pages.append(items[i:i + page_size])
    return pages
