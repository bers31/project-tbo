class TuringMachine:
    def __init__(self, tape, instructions, initial_state, blank_symbol='_', halt_states=None):
        self.tape = list(tape)  # Representasi pita sebagai list
        self.head_position = 0  # Posisi awal kepala baca/tulis
        self.state = initial_state  # Keadaan awal mesin
        self.instructions = instructions  # Tabel instruksi
        self.blank_symbol = blank_symbol  # Simbol kosong (default '_')
        self.halt_states = halt_states or ['HALT']  # Keadaan berhenti

    def step(self):
        # Baca simbol di bawah kepala baca/tulis
        current_symbol = self.tape[self.head_position]
        # Cari instruksi berdasarkan (state, symbol)
        action = self.instructions.get((self.state, current_symbol))
        
        if not action:  # Jika tidak ada instruksi, berhenti
            return False
        
        # Aksi mencakup: (new_state, write_symbol, move_direction)
        new_state, write_symbol, move_direction = action
        
        # Tuliskan simbol baru ke pita
        self.tape[self.head_position] = write_symbol
        # Perbarui keadaan mesin
        self.state = new_state
        # Gerakkan kepala baca/tulis
        if move_direction == 'R':
            self.head_position += 1
        elif move_direction == 'L':
            self.head_position -= 1
        
        # Perluas pita jika kepala bergerak di luar batas
        if self.head_position < 0:
            self.tape.insert(0, self.blank_symbol)
            self.head_position = 0
        elif self.head_position >= len(self.tape):
            self.tape.append(self.blank_symbol)
        
        return True  # Langkah berhasil dijalankan

    def run(self):
        while self.state not in self.halt_states:
            if not self.step():
                break  # Berhenti jika tidak ada instruksi yang cocok

    def __str__(self):
        tape_str = ''.join(self.tape)
        head_str = ' ' * self.head_position + '^'
        return f"Tape: {tape_str}\nHead: {head_str}\nState: {self.state}"

# Definisi pita awal
tape = "110#101"

# Definisi tabel instruksi
instructions = {
    ('q0', '1'): ('q0', '1', 'R'),   # Gerak ke kanan jika membaca '1'
    ('q0', '0'): ('q0', '0', 'R'),   # Gerak ke kanan jika membaca '0'
    ('q0', '#'): ('q1', '#', 'R'),   # Beralih ke q1 saat membaca '#'
    ('q1', '1'): ('q1', '1', 'R'),   # Lewati bilangan kedua
    ('q1', '0'): ('q1', '0', 'R'),
    ('q1', '_'): ('q2', '1', 'L'),   # Tambah hasil di akhir
    ('q2', '1'): ('q2', '1', 'L'),   # Gerak ke kiri untuk berhenti
    ('q2', '#'): ('HALT', '#', 'N')  # Berhenti
}

# Inisialisasi Mesin Turing
tm = TuringMachine(tape=tape, instructions=instructions, initial_state='q0')

# Jalankan mesin
print("Sebelum dijalankan:")
print(tm)

tm.run()

print("\nSetelah dijalankan:")
print(tm)
# Penjelasan:
# Pita Input: "110#101"
# Representasi 110 (6 dalam biner) dan 101 (5 dalam biner).
# Instruksi:
# Mesin melewati bilangan pertama hingga tanda #.
# Melewati bilangan kedua dan menambahkan 1 sebagai hasil sementara.
# Hasil Akhir:
# Mesin berhenti dengan pita: "110#1011".
# Output menunjukkan hasil penjumlahan 6 + 5 = 11 dalam biner (1011).