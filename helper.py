import subprocess
import os
from typing import List, Tuple, Dict

DEFAULT_STATUS = "off"
OUTPUT_FILEPATH = "/tmp/checklist_choices.txt"


def run_tui_checklist(option_tags: List[str], option_texts: List[str]) -> List[str]:

    options_for_dialog = []
    for tag, text in zip(option_tags, option_texts):
        options_for_dialog.extend([tag, text, DEFAULT_STATUS])

    command = [
        "dialog",
        "--title", "Özellik Seçimi",
        "--checklist", "Lütfen etkinleştirmek istediğiniz özellikleri seçin:",
        "15", "50", str(len(option_tags)), 
        *options_for_dialog
    ]
    
    # --- 3. Komutu Çalıştırma ---
    try:
        # Komutu çalıştırır, 'dialog' çıktısını (seçilen TAG'ler) stderr'den yakalar.
        # Bu çıktı, daha sonra okunması için geçici bir dosyaya yazılır.
        result = subprocess.run(
            command,
            stderr=subprocess.PIPE,
            check=False # Dialog iptal edildiğinde (return code 1) hata vermemek için check=False yapıldı
        )
        
        # Dialog çıktısını geçici dosyaya yazar
        with open(OUTPUT_FILEPATH, 'w') as f:
            f.write(result.stderr.decode('utf-8'))

        # Kullanıcı OK'e bastıysa (return code 0) sonuçları işle
        if result.returncode == 0:
            with open(OUTPUT_FILEPATH, 'r') as f:
                raw_choices = f.read().strip()
            
            # Tırnakları kaldırır ve boşluklarla ayrılmış TAG'leri listeye dönüştürür.
            selected_choices = raw_choices.replace('"', '').split()
            
            print(f"\nSeçim başarılı: {len(selected_choices)} özellik seçildi.")
            return selected_choices
        
        # Kullanıcı İptal'e bastıysa (return code 1)
        elif result.returncode == 1:
            print("\nYapılandırma kullanıcı tarafından iptal edildi.")
            return []
        
        else:
            # Diğer hatalar
            print(f"\nKomut çalıştırılırken bir hata oluştu. Hata kodu: {result.returncode}")
            return []


    except FileNotFoundError:
        print("\nHATA: 'dialog' uygulaması bulunamadı.")
        print("Lütfen yükleyin (örneğin, Debian/Ubuntu'da 'sudo apt install dialog').")
        return []
    except Exception as e:
        print(f"\nBeklenmedik bir hata oluştu: {e}")
        return []
        
    finally:
        # Geçici dosyayı temizle
        if os.path.exists(OUTPUT_FILEPATH):
            os.remove(OUTPUT_FILEPATH)
            
if __name__ == "__main__":
    # Örnek kullanım (Dosya doğrudan çalıştırıldığında)
    
    # Kullanıcıdan gelen input'u taklit etmek için örnek veriler
    my_option_tags = ["A", "B", "C"]
    my_option_texts = ["Seçenek Alpha", "Seçenek Beta", "Seçenek Gamma"]
    
    print("--- run_tui_checklist Örnek Çalıştırma ---")
    
    # Fonksiyonu çağır ve sonucu al
    selections = run_tui_checklist(my_option_tags, my_option_texts)
    
    print("\n--- Geri Dönüş Özeti ---")
    if selections:
        print("Seçilen TAG'ler:")
        for tag in selections:
            print(f"- {tag}")
    else:
        print("Hiçbir şey seçilmedi veya işlem iptal edildi.")
