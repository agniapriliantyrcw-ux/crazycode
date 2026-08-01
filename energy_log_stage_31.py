# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: EnergyLog
def switch_profile():
    """Переключение активного пользовательского профиля."""
    import os, json
    
    profiles_dir = "profiles"
    if not os.path.isdir(profiles_dir):
        os.makedirs(profiles_dir)
    
    active_file = f"{profiles_dir}/active.json"
    if not os.path.exists(active_file):
        with open(active_file, 'w') as f:
            json.dump({"name": "default", "color": "#3498db"}, f)
    
    def _load_profiles():
        pro = {}
        for fname in sorted(os.listdir(profiles_dir)):
            if fname.endswith('.json'):
                with open(f"{profiles_dir}/{fname}") as fh:
                    pro[os.path.splitext(fname)[0]] = json.load(fh)
        return pro
    
    def _save_active(name):
        act = {"name": name, "color": "#3498db"}
        with open(active_file, 'w') as f:
            json.dump(act, f)
    
    print("=" * 50)
    profiles = _load_profiles()
    if not profiles:
        print("Нет сохранённых профилей. Создайте файл через add_profile().")
        return
    
    print(f"📋 Доступные профили:")
    for name in sorted(profiles.keys()):
        p = profiles[name]
        marker = " ⭐ АКТИВНЫЙ" if name == _load_profiles()["name"] else ""
        print(f"  • {name}{marker}")
    
    choice = input("\nВыберите профиль (или введите 'new' для создания нового): ").strip() or list(profiles.keys())[0]
    
    if choice.lower() == "new":
        name = input("Имя нового профиля: ").strip().lower()
        color = input(f"Цвет ({'#3498db'}): ").strip() or "#3498db"
        pfile = f"{profiles_dir}/{name}.json"
        with open(pfile, 'w') as f:
            json.dump({"name": name, "color": color}, f)
        _save_active(name)
        print(f"✅ Профиль '{name}' создан и установлен как активный.")
    elif choice in profiles:
        if profile_choice == list(profiles.keys())[0] and list(profiles.values())[0]["name"] != choice:
            _save_active(choice)
            print(f"🔄 Активный профиль изменён на: {choice}")
