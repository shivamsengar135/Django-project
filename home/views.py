from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from home.models import Contact

PRODUCTS = [
    {
        "name": "Belgian Chocolate Scoop",
        "category": "Ice Cream",
        "price": "Rs. 120",
        "description": "Rich cocoa and dark chocolate swirl for true chocolate lovers.",
        "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "name": "Strawberry Bliss Sundae",
        "category": "Ice Cream",
        "price": "Rs. 140",
        "description": "Fresh strawberries, vanilla cream, and crunchy toppings.",
        "image": "https://images.unsplash.com/photo-1488900128323-21503983a07e?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "name": "Mango Kulfi Stick",
        "category": "Frozen Dessert",
        "price": "Rs. 80",
        "description": "Classic Indian-style kulfi with Alphonso mango flavor.",
        "image": "https://images.unsplash.com/photo-1570197788417-0e82375c9371?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "name": "Fresh Farm Milk",
        "category": "Dairy",
        "price": "Rs. 65",
        "description": "Daily fresh pasteurized milk from trusted partner farms.",
        "image": "https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "name": "Hand-Churned Butter",
        "category": "Dairy",
        "price": "Rs. 95",
        "description": "Soft and creamy butter for breakfast and cooking.",
        "image": "/static/images/c.jpg",
    },
    {
        "name": "Party Dessert Box",
        "category": "Events",
        "price": "Rs. 699",
        "description": "Mixed mini cups for birthdays, office treats, and events.",
        "image": "https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?auto=format&fit=crop&w=1200&q=80",
    },
]

SERVICE_PAGES = {
    "ice-cream": {
        "title": "Ice Cream Specials",
        "subtitle": "Creamy scoops, sundaes, kulfi sticks, and seasonal flavors.",
        "hero_image": "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?auto=format&fit=crop&w=1400&q=80",
        "items": [
            {
                "name": "Belgian Chocolate Scoop",
                "description": "Deep cocoa profile with dark chocolate chips.",
                "price": "Rs. 120",
                "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=1200&q=80",
            },
            {
                "name": "Strawberry Bliss Sundae",
                "description": "Fresh strawberry puree with vanilla cream.",
                "price": "Rs. 140",
                "image": "https://images.unsplash.com/photo-1488900128323-21503983a07e?auto=format&fit=crop&w=1200&q=80",
            },
            {
                "name": "Mango Kulfi Stick",
                "description": "Traditional kulfi touch with alphonso mango.",
                "price": "Rs. 80",
                "image": "https://images.unsplash.com/photo-1570197788417-0e82375c9371?auto=format&fit=crop&w=1200&q=80",
            },
            {
                "name": "Party Dessert Box",
                "description": "A mix of mini cups for celebrations.",
                "price": "Rs. 699",
                "image": "https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?auto=format&fit=crop&w=1200&q=80",
            },
        ],
    },
    "milk": {
        "title": "Fresh Milk Collection",
        "subtitle": "Daily-supplied milk variants for homes, cafes, and bakeries.",
        "hero_image": "https://images.unsplash.com/photo-1563636619-e9143da7973b?auto=format&fit=crop&w=1400&q=80",
        "items": [
            {
                "name": "Fresh Farm Milk",
                "description": "Daily pasteurized milk with natural taste.",
                "price": "Rs. 65",
                "image": "https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&fit=crop&w=1200&q=80",
            },
            {
                "name": "Double-Toned Milk",
                "description": "Balanced fat content for regular use.",
                "price": "Rs. 58",
                "image": "https://images.unsplash.com/photo-1517448931760-9bf4414148c5?auto=format&fit=crop&w=1200&q=80",
            },
            {
                "name": "Full Cream Milk",
                "description": "Thicker texture ideal for tea and sweets.",
                "price": "Rs. 72",
                "image": "https://images.unsplash.com/photo-1563636619-e9143da7973b?auto=format&fit=crop&w=1200&q=80",
            },
            {
                "name": "Bulk Morning Delivery Pack",
                "description": "Early doorstep delivery for homes and cafes.",
                "price": "Rs. 499",
                "image": "https://images.unsplash.com/photo-1471193945509-9ad0617afabf?auto=format&fit=crop&w=1200&q=80",
            },
        ],
    },
    "butter": {
        "title": "Butter & Spread Range",
        "subtitle": "Hand-churned and flavored butter packs for breakfast and cooking.",
        "hero_image": "https://images.unsplash.com/photo-1625938144755-652e08e359b7?auto=format&fit=crop&w=1400&q=80",
        "items": [
            {
                "name": "Hand-Churned Butter",
                "description": "Creamy and smooth for daily spreads.",
                "price": "Rs. 95",
                "image": "/static/images/c.jpg",
            },
            {
                "name": "Salted Table Butter",
                "description": "Classic salted cube for breakfast and snacks.",
                "price": "Rs. 110",
                "image": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?auto=format&fit=crop&w=1200&q=80",
            },
            {
                "name": "Garlic Herb Butter",
                "description": "Flavor-packed butter for toast and saute.",
                "price": "Rs. 130",
                "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=1200&q=80",
            },
            {
                "name": "Unsalted Baking Butter",
                "description": "Ideal for cakes, cookies, and pastries.",
                "price": "Rs. 125",
                "image": "https://images.unsplash.com/photo-1558211583-d26f610c1eb1?auto=format&fit=crop&w=1200&q=80",
            },
        ],
    },
}

PAGES = [
    {"name": "Home", "url": "/", "keywords": "landing featured hero"},
    {"name": "About", "url": "/about/", "keywords": "story mission quality"},
    {"name": "Services", "url": "/services/", "keywords": "products dairy events"},
    {"name": "Contact", "url": "/contact/", "keywords": "email phone message"},
    {"name": "Register", "url": "/register/", "keywords": "signup account"},
    {"name": "Login", "url": "/login/", "keywords": "signin account"},
]


def index(request):
    context = {
        "featured_products": PRODUCTS[:3],
        "top_products": PRODUCTS,
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact_data = Contact(
            name=name, email=email, phone=phone, desc=desc, date=datetime.today()
        )
        contact_data.save()
        messages.success(request, "Your message has been sent successfully!")
    return render(request, "contact.html")


def services(request):
    service_sections = []
    for slug, page in SERVICE_PAGES.items():
        service_sections.append(
            {
                "slug": slug,
                "title": page["title"],
                "subtitle": page["subtitle"],
                "items": page["items"],
            }
        )
    return render(
        request,
        "services.html",
        {"products": PRODUCTS, "service_sections": service_sections},
    )


def service_detail(request, category):
    page = SERVICE_PAGES.get(category)
    if not page:
        messages.error(request, "Service category not found.")
        return redirect("services")
    return render(request, "service_detail.html", {"page": page})


def search(request):
    query = request.GET.get("q", "").strip()
    product_results = []
    page_results = []

    if query:
        query_lower = query.lower()
        for product in PRODUCTS:
            text_blob = " ".join(
                [product["name"], product["category"], product["description"]]
            ).lower()
            if query_lower in text_blob:
                product_results.append(product)

        for page in PAGES:
            text_blob = f"{page['name']} {page['keywords']}".lower()
            if query_lower in text_blob:
                page_results.append(page)

    context = {
        "query": query,
        "product_results": product_results,
        "page_results": page_results,
        "total_results": len(product_results) + len(page_results),
    }
    return render(request, "search.html", context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Registration successful. Please login.")
            return redirect("login")

    return render(request, "register.html")


def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("home")

        messages.error(request, "Invalid username or password.")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("home")
