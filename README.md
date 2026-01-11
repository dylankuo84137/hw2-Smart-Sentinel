# G12 程式設計進階 - 作業二：智慧哨兵 (Smart Sentinel)

這份儲存庫是「G12 程式設計進階」課程的第二次作業：智慧哨兵。
在這個作業中，我們將結合感測器輸入與 LCD 顯示，打造一個能夠「獨立運作」並「自我表達」的環境監測裝置。

- **課程**：G12 程式設計進階 (Advanced Programming Techniques)
- **作業**：HW2 - Smart Sentinel
- **繳交者**：(請填寫你的姓名)

---

### 題目說明

請使用 Python (MicroPython) 撰寫一個環境監測程式，並整合 ESP32 硬體。程式的邏輯目標如下：

1.  **Input**: 讀取感測器數值 (如光敏電阻、距離感測器、溫度感測器等)。
2.  **Output**: 將讀取到的數值透過 LCD 顯示出來。
3.  **Process**: 根據數值進行邏輯判斷，給予使用者對應的狀態回饋。

### 功能實作要求

*   **[Must]** 程式啟動時，LCD 必須顯示你的這支程式的名稱或作者 (Splash Screen/開機畫面)。
*   **[Must]** 進入迴圈後，持續讀取某個感測器的數值。
*   **[Must]** 根據數值，在 LCD 上顯示 **「目前數值」** 以及 **「狀態文字」**。
*   **[Level 2/3]** 能夠根據數值判斷情境（如：「太亮」、「太暗」、「正常」）。
*   **[Level 3]** 能夠以視覺化方式呈現數據（如：進度條、自定義圖案、或閃爍背光）。

### 硬體接線範例 (請根據實際情況修改)

| 元件 | ESP32 腳位 | 備註 |
| :--- | :--- | :--- |
| **感測器 (Sensor)** | GPIO 34 | 類比輸入 (Analog Input) |
| **LCD SDA** | GPIO 21 | I2C 資料線 |
| **LCD SCL** | GPIO 22 | I2C 時脈線 |
| **VCC/GND** | 3.3V / GND | 共地 |

### 執行範例 (LCD 顯示內容)

**Level 1: 實習生 (Apprentice)**
```
Light Level:
Val: 2045
```

**Level 2: 工程師 (Engineer)**
```
Val: 3500
Too Bright!
```

**Level 3: 駭客 (Hacker)**
```
Light: 3500
#############
```

### 如何執行

1.  請確保你的 ESP32 已燒錄 MicroPython 韌體。
2.  將 `lcd_api.py` 與 `esp8266_i2c_lcd.py` 上傳至開發板。
3.  將 `main.py` 上傳至開發板。
4.  按下 ESP32 的 **Reset** 按鈕，即可看到執行結果。

---

### Commit 紀錄建議

根據課程說明，良好的 `commit` 紀錄是學習歷程的一部分。你可以參考以下格式來撰寫你的 commit 訊息：

*   `feat: 完成開機畫面 (Splash Screen)`
*   `feat: 成功讀取光敏電阻數值`
*   `feat: 完成 LCD 數值顯示功能`
*   `feat: 加入狀態判斷邏輯 (Too Bright/Too Dark)`
*   `style: 優化 LCD 顯示排版`
*   `docs: 新增硬體接線說明至 README`

祝你玩得開心！
