# ==========================================================
# INTERFACE GRÁFICA (Tkinter) para o Agente de Irrigação
# Visual colorido e mais intuitivo
# Requer o arquivo agente_irrigacao.py na mesma pasta
# ==========================================================

import tkinter as tk
from tkinter import ttk, messagebox
from agente_irrigacao import decidir_irrigacao, simular, LIMIARES

# ---------------- PALETA DE CORES ----------------
COR_FUNDO = "#EAF6EF"        # verde bem claro (fundo geral)
COR_HEADER = "#2E7D32"       # verde escuro (cabeçalho)
COR_HEADER_TEXTO = "#FFFFFF"
COR_CARD = "#FFFFFF"
COR_BOTAO = "#43A047"        # verde médio
COR_BOTAO_HOVER = "#2E7D32"
COR_BOTAO_TEXTO = "#FFFFFF"
COR_LIGAR = "#2E7D32"        # verde forte -> irrigação ligada
COR_NAO_LIGAR = "#EF6C00"    # laranja -> irrigação não necessária
COR_TITULO_ABA = "#1565C0"   # azul para títulos internos
COR_TEXTO = "#263238"


class AgenteIrrigacaoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🌱 Agente de Irrigação Automática")
        self.root.geometry("560x600")
        self.root.configure(bg=COR_FUNDO)
        self.root.resizable(False, False)

        self._configurar_estilos()
        self._montar_header()

        notebook = ttk.Notebook(root, style="Custom.TNotebook")
        notebook.pack(fill="both", expand=True, padx=15, pady=15)

        self.aba_manual = tk.Frame(notebook, bg=COR_CARD)
        self.aba_simulacao = tk.Frame(notebook, bg=COR_CARD)
        self.aba_limiares = tk.Frame(notebook, bg=COR_CARD)

        notebook.add(self.aba_manual, text="  🔍 Verificar Agora  ")
        notebook.add(self.aba_simulacao, text="  📊 Simulação  ")
        notebook.add(self.aba_limiares, text="  ⚙️ Configurações  ")

        self._montar_aba_manual()
        self._montar_aba_simulacao()
        self._montar_aba_limiares()

    # ---------------- ESTILOS GERAIS ----------------
    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Custom.TNotebook", background=COR_FUNDO, borderwidth=0)
        style.configure(
            "Custom.TNotebook.Tab",
            font=("Segoe UI", 10, "bold"),
            padding=[12, 8],
            background="#C8E6C9",
            foreground=COR_TEXTO
        )
        style.map(
            "Custom.TNotebook.Tab",
            background=[("selected", COR_HEADER)],
            foreground=[("selected", "#FFFFFF")]
        )

    # ---------------- CABEÇALHO ----------------
    def _montar_header(self):
        header = tk.Frame(self.root, bg=COR_HEADER, height=80)
        header.pack(fill="x", side="top")

        tk.Label(
            header, text="🌿 Agente de Irrigação Automática",
            font=("Segoe UI", 16, "bold"), bg=COR_HEADER, fg=COR_HEADER_TEXTO
        ).pack(pady=(15, 0))

        tk.Label(
            header, text="Decide quando ligar a irrigação com base em temperatura, umidade e chuva",
            font=("Segoe UI", 9), bg=COR_HEADER, fg="#E8F5E9"
        ).pack(pady=(0, 12))

    # ---------------- BOTÃO ESTILIZADO ----------------
    def _criar_botao(self, parent, texto, comando):
        botao = tk.Button(
            parent, text=texto, command=comando,
            font=("Segoe UI", 10, "bold"), bg=COR_BOTAO, fg=COR_BOTAO_TEXTO,
            activebackground=COR_BOTAO_HOVER, activeforeground="white",
            relief="flat", padx=14, pady=8, cursor="hand2", bd=0
        )
        return botao

    # ---------------- ABA 1: entrada manual ----------------
    def _montar_aba_manual(self):
        frame = self.aba_manual
        frame.configure(padx=20, pady=20)

        tk.Label(
            frame, text="Informe os dados do momento:",
            font=("Segoe UI", 11, "bold"), bg=COR_CARD, fg=COR_TITULO_ABA
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 15))

        campos = [
            ("🌡️ Temperatura (°C)", "entry_temp"),
            ("💧 Umidade do solo (%)", "entry_solo"),
            ("💨 Umidade do ar (%)", "entry_ar"),
        ]
        for i, (rotulo, nome) in enumerate(campos, start=1):
            tk.Label(frame, text=rotulo, font=("Segoe UI", 10), bg=COR_CARD, fg=COR_TEXTO).grid(
                row=i, column=0, sticky="w", pady=8
            )
            entry = tk.Entry(frame, font=("Segoe UI", 10), relief="solid", bd=1, width=15)
            entry.grid(row=i, column=1, sticky="w", padx=10)
            setattr(self, nome, entry)

        self.var_chuva = tk.BooleanVar()
        tk.Checkbutton(
            frame, text="🌧️ Previsão de chuva", variable=self.var_chuva,
            font=("Segoe UI", 10), bg=COR_CARD, fg=COR_TEXTO,
            activebackground=COR_CARD, selectcolor=COR_CARD
        ).grid(row=4, column=0, columnspan=2, sticky="w", pady=10)

        self._criar_botao(frame, "Verificar decisão", self._verificar_manual).grid(
            row=5, column=0, columnspan=2, pady=15, sticky="we"
        )

        self.resultado_frame = tk.Frame(frame, bg="#F1F8E9", relief="solid", bd=1)
        self.resultado_frame.grid(row=6, column=0, columnspan=2, sticky="we", pady=10)

        self.resultado_label = tk.Label(
            self.resultado_frame, text="Preencha os campos e clique em Verificar",
            font=("Segoe UI", 11, "bold"), bg="#F1F8E9", fg=COR_TEXTO,
            wraplength=440, justify="left", padx=10, pady=12
        )
        self.resultado_label.pack(fill="both")

    def _verificar_manual(self):
        try:
            dados = {
                "temperatura": float(self.entry_temp.get()),
                "umidade_solo": float(self.entry_solo.get()),
                "umidade_ar": float(self.entry_ar.get()),
                "previsao_chuva": self.var_chuva.get()
            }
        except ValueError:
            messagebox.showerror("Erro", "Preencha temperatura e umidades com números válidos.")
            return

        ligou, motivo = decidir_irrigacao(
            dados,
            limiar_umidade_solo=LIMIARES["umidade_solo"],
            limiar_temp_alta=LIMIARES["temp_alta"]
        )

        if ligou:
            texto = f"🟢 LIGAR IRRIGAÇÃO\n{motivo}"
            cor = COR_LIGAR
        else:
            texto = f"🟠 NÃO LIGAR\n{motivo}"
            cor = COR_NAO_LIGAR

        self.resultado_label.config(text=texto, fg=cor)

    # ---------------- ABA 2: simulação ----------------
    def _montar_aba_simulacao(self):
        frame = self.aba_simulacao
        frame.configure(padx=20, pady=20)

        tk.Label(
            frame, text="Simular vários dias de uma vez:",
            font=("Segoe UI", 11, "bold"), bg=COR_CARD, fg=COR_TITULO_ABA
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 15))

        tk.Label(frame, text="📅 Quantidade de dias", font=("Segoe UI", 10), bg=COR_CARD, fg=COR_TEXTO).grid(
            row=1, column=0, sticky="w"
        )
        self.entry_dias = tk.Entry(frame, font=("Segoe UI", 10), relief="solid", bd=1, width=10)
        self.entry_dias.insert(0, "30")
        self.entry_dias.grid(row=1, column=1, sticky="w", padx=10)

        self._criar_botao(frame, "Rodar simulação", self._rodar_simulacao).grid(
            row=2, column=0, columnspan=2, pady=15, sticky="we"
        )

        self.resumo_label = tk.Label(
            frame, text="", font=("Segoe UI", 10, "bold"), bg=COR_CARD, fg=COR_TITULO_ABA
        )
        self.resumo_label.grid(row=3, column=0, columnspan=2, sticky="w", pady=(0, 8))

        self.texto_resultado = tk.Text(
            frame, width=58, height=16, font=("Consolas", 9),
            bg="#FAFAFA", relief="solid", bd=1
        )
        self.texto_resultado.grid(row=4, column=0, columnspan=2)
        self.texto_resultado.tag_config("ligou", foreground=COR_LIGAR)
        self.texto_resultado.tag_config("nao_ligou", foreground=COR_NAO_LIGAR)

    def _rodar_simulacao(self):
        try:
            dias = int(self.entry_dias.get())
        except ValueError:
            messagebox.showerror("Erro", "Informe um número inteiro de dias.")
            return

        historico = simular(dias)
        dias_irrigados = sum(1 for d in historico if d["irrigou"])

        self.resumo_label.config(
            text=f"💧 Irrigação ligada em {dias_irrigados} de {dias} dias ({dias_irrigados/dias:.0%})"
        )

        self.texto_resultado.delete("1.0", tk.END)
        for registro in historico[:20]:
            status = "LIGOU  " if registro["irrigou"] else "não ligou"
            tag = "ligou" if registro["irrigou"] else "nao_ligou"
            linha = (f"Dia {registro['dia']:>3}: temp={registro['temperatura']:>5}°C  "
                     f"solo={registro['umidade_solo']:>5}%  chuva={str(registro['previsao_chuva']):<5}  "
                     f"-> {status}\n")
            self.texto_resultado.insert(tk.END, linha, tag)

    # ---------------- ABA 3: limiares ----------------
    def _montar_aba_limiares(self):
        frame = self.aba_limiares
        frame.configure(padx=20, pady=20)

        tk.Label(
            frame, text="Ajustar sensibilidade do agente:",
            font=("Segoe UI", 11, "bold"), bg=COR_CARD, fg=COR_TITULO_ABA
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 15))

        tk.Label(
            frame, text="💧 Ligar irrigação quando o solo estiver abaixo de (%):",
            font=("Segoe UI", 10), bg=COR_CARD, fg=COR_TEXTO, wraplength=280, justify="left"
        ).grid(row=1, column=0, sticky="w", pady=10)
        self.entry_limiar_solo = tk.Entry(frame, font=("Segoe UI", 10), relief="solid", bd=1, width=10)
        self.entry_limiar_solo.insert(0, str(LIMIARES["umidade_solo"]))
        self.entry_limiar_solo.grid(row=1, column=1, padx=10)

        tk.Label(
            frame, text="🌡️ Considerar calor intenso acima de (°C):",
            font=("Segoe UI", 10), bg=COR_CARD, fg=COR_TEXTO, wraplength=280, justify="left"
        ).grid(row=2, column=0, sticky="w", pady=10)
        self.entry_limiar_temp = tk.Entry(frame, font=("Segoe UI", 10), relief="solid", bd=1, width=10)
        self.entry_limiar_temp.insert(0, str(LIMIARES["temp_alta"]))
        self.entry_limiar_temp.grid(row=2, column=1, padx=10)

        self._criar_botao(frame, "Salvar configurações", self._salvar_limiares).grid(
            row=3, column=0, columnspan=2, pady=20, sticky="we"
        )

    def _salvar_limiares(self):
        try:
            LIMIARES["umidade_solo"] = float(self.entry_limiar_solo.get())
            LIMIARES["temp_alta"] = float(self.entry_limiar_temp.get())
            messagebox.showinfo("Sucesso", "Configurações atualizadas!")
        except ValueError:
            messagebox.showerror("Erro", "Valores inválidos.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgenteIrrigacaoGUI(root)
    root.mainloop()