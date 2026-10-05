from chatbot.knowledge import get_related_options, get_subtopic_options, search_answer


def test_search_answer_returns_default_topic_result():
    result = search_answer("account opening")
    assert result is not None
    assert result["title"] == "Account Opening"
    assert isinstance(result["answer"], list)
    assert len(result["answer"]) > 0


def test_get_related_options_returns_customer_help_menu():
    options = get_related_options("Account Opening")
    assert options
    assert any(option["id"] == "overview" for option in options)
    assert any(option["id"] == "documents" for option in options)

    result = search_answer("Account Opening", "documents")
    assert result is not None
    assert result["title"] == "Account Opening"
    assert any("Aadhaar" in paragraph for paragraph in result["answer"])


def test_get_subtopic_options_returns_service_specific_options():
    options = get_subtopic_options("Account Opening")
    assert options
    assert any(option["id"] == "savings_account" for option in options)
    assert any(option["id"] == "salary_account" for option in options)

    result = search_answer("Account Opening", "savings_account")
    assert result is not None
    assert result["title"] == "Savings Account"
    assert any("interest" in paragraph.lower() for paragraph in result["answer"])
