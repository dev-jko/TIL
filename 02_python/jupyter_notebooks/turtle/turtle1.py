import turtle as t


class MagicBrush:

    def set_color(self, my_color):
        t.color(my_color)

    def go_right(self, a, b, n):
        for _ in range(n):
            t.forward(a)
            t.right(b)

    def go_left(self, a, b, n):
        for _ in range(n):
            t.forward(a)
            t.left(b)

    def draw_square(self, ):
        self.go_right(100, 90, 4)

    def draw_triangle(self, ):
        self.go_left(100, 120, 3)


brad = t.Turtle()
brad.shape('turtle')
brad.speed(2)
brad.forward(100)


m = MagicBrush()
m.draw_square()
t.left(120)
m.draw_triangle()
t.mainloop()
