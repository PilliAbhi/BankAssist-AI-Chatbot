import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

with open(
    BASE_DIR / "knowledge" / "banking_knowledge.json",
    "r",
    encoding="utf-8"
) as file:

    KNOWLEDGE = json.load(file)


MENU_OPTIONS = [
    {"id": "overview", "label": "Overview"},
    {"id": "documents", "label": "Documents Required"},
    {"id": "steps", "label": "Process & Steps"},
    {"id": "support", "label": "Support & Safety"},
]


SERVICE_SUBTOPICS = {
    "account_opening": [
        {
            "id": "savings_account",
            "label": "Savings Account",
            "title": "Savings Account",
            "answer": [
                "A savings account is designed for regular deposits and everyday financial security. It helps customers store money safely while earning interest on the balance.",
                "The interest rate depends on the bank's policy, the account type, and the customer profile. Most banks also allow free or low-cost digital banking, fund transfers, and SMS alerts with this account.",
                "Savings accounts usually come with an ATM or debit card, mobile banking access, and a cheque book. They are ideal for emergency savings, household budgeting, and short-term financial planning.",
                "Key points: Suitable for everyday banking; earns interest on deposits; includes ATM access, account alerts, and digital transactions; charges may apply for non-maintenance or extra services."
            ]
        },
        {
            "id": "salary_account",
            "label": "Salary Account",
            "title": "Salary Account",
            "answer": [
                "A salary account is opened for employees whose salary is credited directly by their employer. These accounts usually offer better benefits such as zero-balance features, discounted credit cards, and lower service charges.",
                "Many banks provide cashback, free transactions, and special customer assistance for salary account holders. The account is often linked with direct deposit and payroll processing.",
                "Benefits often include easier access to online banking, mobile app features, ATM cards, and dedicated support. This makes it a convenient option for salaried customers who need quick access to funds.",
                "Key points: Salary accounts are employer-linked; they often include recurring benefits, free transactions, and value-added services; customers can use them for direct salary credit and everyday expenses."
            ]
        },
        {
            "id": "current_account",
            "label": "Current Account",
            "title": "Current Account",
            "answer": [
                "A current account is mainly meant for businesses, self-employed professionals, and frequent transaction users. It supports high-volume deposits, withdrawals, and payments without strict balance restrictions.",
                "This account is preferred by traders, companies, and entrepreneurs because it allows large-scale cash movement and business-related transactions. Banks may provide cheque books, internet banking, and dedicated business support.",
                "Current accounts may require a higher minimum balance and may be subject to account maintenance charges depending on the bank. They are built for convenience, operational flexibility, and regular business funds management.",
                "Key points: Best for business banking; supports frequent cash movement; may have higher minimum balance and account charges; includes cheque and digital business features."
            ]
        }
    ],
    "minimum_balance": [
        {
            "id": "regular_savings",
            "label": "Regular Savings",
            "title": "Regular Savings Balance",
            "answer": [
                "Regular savings accounts usually require a minimum balance to avoid service charges. Banks set this requirement based on the branch, account type, and customer segment.",
                "If the balance falls below the threshold, the account may attract a maintenance fee or penalty. This is one of the most common reasons customers receive account-related alerts.",
                "To avoid charges, customers should monitor their account activity, maintain a buffer in their balance, and use online banking alerts for upcoming low-balance reminders.",
                "Key points: Minimum balance helps reduce service charges; regular vigilance prevents penalty fees; digital alerts help maintain the account balance."
            ]
        },
        {
            "id": "zero_balance",
            "label": "Zero Balance Account",
            "title": "Zero Balance Account",
            "answer": [
                "A zero-balance account allows customers to operate an account without maintaining a minimum balance. It is commonly offered to students, first-time customers, or specific government-linked benefits.",
                "This type of account is designed to make banking easier for individuals who may not be able to maintain a higher balance. It often comes with limited privileges or lower transaction features depending on the bank policy.",
                "Customers still need to follow KYC rules and may have restrictions on cheque issuance or premium features. Zero-balance accounts are helpful for accessibility and digital-first banking.",
                "Key points: No minimum balance required; useful for beginners and specific customer groups; transaction features may vary by bank policy."
            ]
        }
    ],
    "atm_card": [
        {
            "id": "debit_card",
            "label": "Debit Card",
            "title": "Debit Card",
            "answer": [
                "A debit card is linked directly to your bank account and is used for cash withdrawals, purchases, and point-of-sale transactions. The amount is deducted immediately from the available balance.",
                "It is a very common tool for daily spending and cash access. Banks often include contactless features, ATM withdrawal limits, and secure PIN-based verification.",
                "Customers should keep their debit card and PIN secure. If the card is lost or stolen, it should be blocked immediately to prevent unauthorized access to funds.",
                "Key points: Linked to the account balance; useful for everyday payments; must be protected with a secure PIN and quick blocking when lost."
            ]
        },
        {
            "id": "ru_pay_card",
            "label": "RuPay Card",
            "title": "RuPay Card",
            "answer": [
                "RuPay is a domestic card network used widely in India for ATM and payment transactions. It is accepted for cash withdrawals, online payments, and merchant transactions depending on the bank and merchant network.",
                "It is popular because it provides affordable payment access and supports secure banking transactions. Many banks issue RuPay debit cards as a default option for account holders.",
                "The card works with ATMs and payment terminals, but cardholders should still follow safe usage practices such as not sharing the PIN and monitoring transactions regularly.",
                "Key points: Domestic payment network; supports ATM and merchant transactions; good for everyday banking and low-cost access."
            ]
        }
    ],
    "credit_card": [
        {
            "id": "rewards_card",
            "label": "Rewards Card",
            "title": "Rewards Card",
            "answer": [
                "A rewards credit card gives cashback, airport lounge access, discounts, or reward points on purchases. It is useful for customers who spend regularly and want value from everyday transactions.",
                "Banks often tie reward benefits to categories such as shopping, travel, dining, and fuel. Customers can redeem points for vouchers, statement credits, or travel benefits depending on the program.",
                "Credit cards are useful when used responsibly, but carrying a revolving balance can lead to high interest charges. It is best to pay the bill in full whenever possible.",
                "Key points: Point-based or cashback benefits; good for regular spenders; timely repayment helps avoid high-interest burdens."
            ]
        },
        {
            "id": "travel_card",
            "label": "Travel Card",
            "title": "Travel Card",
            "answer": [
                "A travel credit card is meant for frequent flyers and international travelers. It often provides benefits such as air miles, airport lounge access, foreign exchange convenience, and travel insurance.",
                "These cards are designed for customers who regularly book flights, hotels, and international transactions. The annual fees may be higher, but the rewards may offset the cost for frequent travelers.",
                "To get the best value, users should compare annual charges, conversion fees, and reward redemption rules before choosing a card. This helps avoid paying a premium for features not needed.",
                "Key points: Travel advantages include lounge access and reward points; best for frequent international travelers; check forex and annual fee details before applying."
            ]
        }
    ],
    "upi": [
        {
            "id": "bank_linked_upi",
            "label": "Bank-Linked UPI",
            "title": "Bank-Linked UPI",
            "answer": [
                "Bank-linked UPI lets you link your account directly to a UPI app and send or receive money instantly. It is one of the most popular payment systems for daily transactions.",
                "It supports peer-to-peer transfers, merchant payments, bill payments, and instant purchases. Since the payment is made using your linked bank account, it is fast and convenient.",
                "Security depends on how carefully you protect your device and UPI PIN. Never share the OTP, PIN, or app credentials with anyone, even if the request appears to come from a bank or a trusted contact.",
                "Key points: Fast real-time transfers; linked to your account; secure if you protect your device and never share the UPI PIN."
            ]
        },
        {
            "id": "qr_payment",
            "label": "QR Payment",
            "title": "QR Payment",
            "answer": [
                "A QR payment allows you to scan a merchant QR code and pay instantly using the UPI app. It is commonly used in stores, kiosks, local markets, and online checkout.",
                "This option is convenient because the payment is completed in seconds without needing any physical cash or cards. It is especially useful for small and medium businesses that want faster payments.",
                "Before confirming, customers should verify the merchant name and the amount displayed on the QR payment screen. This helps prevent mistakes, duplicate payments, or scam attempts.",
                "Key points: Fast merchant payment using QR codes; common in retail and daily purchases; always verify the payee and amount before confirming."
            ]
        }
    ],
    "kyc": [
        {
            "id": "aadhaar_kyc",
            "label": "Aadhaar KYC",
            "title": "Aadhaar KYC",
            "answer": [
                "Aadhaar-based KYC is commonly used for identity verification when opening a bank account, applying for a loan, or updating personal details. It helps confirm the customer's identity and address reliably.",
                "The bank may ask for the Aadhaar number, a linked mobile number, and a copy of the document for verification. This helps match the application with the actual customer record.",
                "Aadhaar details should be kept secure and shared only through official bank channels. Customers must be careful about phishing attempts pretending to request KYC information.",
                "Key points: Helps verify identity and address; required for many banking services; only share details through official bank portals or branch visits."
            ]
        },
        {
            "id": "address_update",
            "label": "Address Update",
            "title": "Address Update",
            "answer": [
                "Address updates are needed when a customer changes residence, moves to a new city, or updates a new proof of address. Banks normally ask for a valid address proof such as utility bills, rental agreement, or government documents.",
                "Updating your address ensures your bank records remain accurate and helps avoid issues with correspondence, debit card delivery, or notice service. It also helps maintain compliance with KYC guidelines.",
                "Some banks may ask for a self-declaration letter along with the address proof. This is a routine process and can usually be done at a branch or through the bank's digital portal.",
                "Key points: Keeps account records current; maintains compliance; new address proof may be required before activation or approval."
            ]
        }
    ],
    "fixed_deposit": [
        {
            "id": "regular_fd",
            "label": "Regular FD",
            "title": "Regular Fixed Deposit",
            "answer": [
                "A regular fixed deposit is a commonly used savings option where the customer deposits a lump sum for a fixed period and receives guaranteed interest. It offers predictable returns and lower risk compared to market-linked investment products.",
                "The interest rate depends on the tenure and the bank's current policy. Short-, medium-, and long-term FDs differ in returns, liquidity, and compounding benefits.",
                "This option is ideal for customers who prefer stability and capital protection. Premature withdrawal is usually allowed with some penalty or reduced interest earning.",
                "Key points: Safe and predictable returns; interest depends on tenure and bank policy; early closure may reduce interest or attract charges."
            ]
        },
        {
            "id": "senior_citizen_fd",
            "label": "Senior Citizen FD",
            "title": "Senior Citizen Fixed Deposit",
            "answer": [
                "Senior citizen fixed deposits are designed for retirees and older customers who prefer stable and secure returns. Banks often offer higher interest rates for this category to support long-term financial stability.",
                "These deposits help retirees plan secondary income and maintain a clear monthly or quarterly interest payout. The account may have special documentation and age verification requirements.",
                "Banks usually offer specific forms and forms of auto-renewal for senior citizens. This makes it easier to maintain a steady investment stream without constant manual renewal.",
                "Key points: Higher interest rates may be offered; suitable for retirement income; verification and documentation are usually straightforward."
            ]
        }
    ]
}


SERVICE_DOCUMENT_HINTS = {
    "account_opening": ["Aadhaar", "PAN", "address proof", "passport-size photo"],
    "kyc": ["Aadhaar", "PAN", "address proof", "signature"],
    "credit_card": ["income proof", "identity proof", "address proof", "bank statements"],
    "home_loan": ["income proof", "property papers", "identity proof", "address proof"],
    "education_loan": ["admission letter", "fee structure", "identity proof", "guardian income proof"],
    "personal_loan": ["income proof", "employment details", "identity proof", "address proof"],
    "vehicle_loan": ["income proof", "vehicle quotation", "identity proof", "address proof"],
    "gold_loan": ["gold certificates", "identity proof", "address proof", "bank account details"],
    "fixed_deposit": ["PAN", "identity proof", "address proof", "bank account details"],
}


def normalize_key(value):
    return re.sub(r"[^a-z0-9]+", "_", str(value).lower()).strip("_")


def find_service_key(question):
    normalized = normalize_key(question)

    for key in KNOWLEDGE:
        key_normalized = normalize_key(key)
        if normalized == key_normalized or normalized in key_normalized or key_normalized in normalized:
            return key

    return None


def _build_document_answer(service_key, title):
    hints = SERVICE_DOCUMENT_HINTS.get(service_key, ["identity proof", "address proof", "account details"])
    return [
        f"To proceed with {title.lower()}, keep the commonly required documents ready such as {', '.join(hints[:4])}.",
        "Most banks verify these documents before activating a product or service, so it helps to keep them prepared in advance.",
        "If the bank has additional checks, it may ask for a recent photograph, an initial deposit, or a declaration form depending on the account type or service.",
    ]


def _build_steps_answer(service_key, title):
    service_label = title.lower()
    return [
        f"The customer journey for {service_label} usually starts with a request and a quick eligibility check.",
        "After that, the bank validates the customer's KYC, confirms the required documents, and approves the request if everything is in order.",
        "Once the verification is complete, the service is activated and the customer can begin using the product or facility without delay.",
    ]


def _build_support_answer(service_key, title):
    return [
        f"If you need help with {title.lower()}, contact your bank's official customer support, visit a nearby branch, or use the verified banking app for assistance.",
        "Always confirm that you are using the bank's official helpline or website before sharing personal or account information, especially for password resets or KYC updates.",
        "Keeping your mobile number and email updated helps you receive alerts, verification codes, and important service updates promptly.",
    ]


def get_related_options(question):
    service_key = find_service_key(question)
    if service_key is None:
        return []

    return [dict(option) for option in MENU_OPTIONS]


def get_subtopic_options(question):
    service_key = find_service_key(question)
    if service_key is None:
        return []

    return [
        {"id": item["id"], "label": item["label"]}
        for item in SERVICE_SUBTOPICS.get(service_key, [])
    ]


def search_answer(question, option_id=None):
    service_key = find_service_key(question)
    if service_key is None:
        return None

    subtopic_list = SERVICE_SUBTOPICS.get(service_key, [])
    subtopic_map = {item["id"]: item for item in subtopic_list}

    entry = KNOWLEDGE[service_key]
    title = entry.get("title")
    default_answer = entry.get("answer", [])

    if option_id in subtopic_map:
        selected = subtopic_map[option_id]
        return {"title": selected.get("title", title), "answer": selected.get("answer", default_answer)}

    if option_id == "documents":
        return {"title": title, "answer": _build_document_answer(service_key, title)}

    if option_id == "steps":
        return {"title": title, "answer": _build_steps_answer(service_key, title)}

    if option_id == "support":
        return {"title": title, "answer": _build_support_answer(service_key, title)}

    if option_id == "overview":
        return {"title": title, "answer": default_answer}

    return {"title": title, "answer": default_answer}
