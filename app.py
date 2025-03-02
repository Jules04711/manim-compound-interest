from manim import *
import numpy as np

class CompoundInterestExplanation(Scene):
    def construct(self):
        # Title and introduction
        title = Text("Understanding Compound Interest", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Define our variables
        principal_value = 1000
        interest_rate = 0.1  # 10%
        years = 5
        
        # Basic definition
        definition = Text("Compound interest is interest on both:", font_size=32)
        definition.next_to(title, DOWN, buff=0.75)
        
        bullets = VGroup(
            Text("• The initial principal", font_size=28),
            Text("• Previously accumulated interest", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT)
        bullets.next_to(definition, DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(Write(definition))
        self.play(Write(bullets), run_time=2)
        self.wait(1)
        
        # Clear screen for formula introduction
        self.play(
            FadeOut(definition),
            FadeOut(bullets)
        )
        
        # Formula explanation
        formula_title = Text("The Formula", font_size=36)
        formula_title.next_to(title, DOWN, buff=0.75)
        
        formula = MathTex(
            r"\text{Compound Interest} = P [(1 + i)^n - 1]",
            font_size=40
        )
        formula.next_to(formula_title, DOWN, buff=0.5)
        
        variables = VGroup(
            MathTex(r"P = \text{principal (initial investment)}", font_size=28),
            MathTex(r"i = \text{annual interest rate (decimal)}", font_size=28),
            MathTex(r"n = \text{number of compounding periods}", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT)
        variables.next_to(formula, DOWN, buff=0.75)
        
        self.play(Write(formula_title))
        self.play(Write(formula))
        self.play(Write(variables), run_time=2)
        self.wait(2)
        
        # Clear for visualization
        self.play(
            FadeOut(formula_title),
            FadeOut(formula),
            FadeOut(variables)
        )
        
        # Setup our example
        example_text = Text(f"Example: ${principal_value} invested at {interest_rate*100}% for {years} years", font_size=32)
        example_text.next_to(title, DOWN, buff=0.75)
        
        self.play(Write(example_text))
        self.wait(1)
        
        # Create axes for our graph
        axes = Axes(
            x_range=[0, years+0.5, 1],
            y_range=[0, 2000, 500],
            axis_config={"include_tip": False},
            x_axis_config={"label_direction": DOWN},
            y_axis_config={"label_direction": LEFT}
        )
        
        axes.add_coordinates()
        
        x_label = Text("Years", font_size=24).next_to(axes.x_axis, DOWN)
        y_label = Text("Amount ($)", font_size=24).next_to(axes.y_axis, LEFT).rotate(90 * DEGREES)
        
        graph_group = VGroup(axes, x_label, y_label)
        graph_group.scale(0.8)
        graph_group.to_edge(DOWN, buff=0.5)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # Plot simple interest for comparison
        simple_amounts = [principal_value * (1 + interest_rate * year) for year in range(years + 1)]
        simple_points = [axes.coords_to_point(year, amount) for year, amount in enumerate(simple_amounts)]
        simple_dots = VGroup(*[Dot(point, color=BLUE) for point in simple_points])
        
        simple_line = Line(simple_points[0], simple_points[-1], color=BLUE)
        simple_label = Text("Simple Interest", font_size=20, color=BLUE)
        simple_label.next_to(simple_line.get_end(), RIGHT)
        
        # Plot compound interest
        compound_amounts = [principal_value * (1 + interest_rate) ** year for year in range(years + 1)]
        compound_points = [axes.coords_to_point(year, amount) for year, amount in enumerate(compound_amounts)]
        compound_dots = VGroup(*[Dot(point, color=GREEN) for point in compound_points])
        
        compound_graph = VMobject(color=GREEN)
        compound_graph.set_points_smoothly(compound_points)
        compound_label = Text("Compound Interest", font_size=20, color=GREEN)
        compound_label.next_to(compound_graph.get_end(), RIGHT)
        
        # Animation sequence
        # First show simple interest
        self.play(FadeIn(simple_dots[0]))
        starting_dot_label = Text(f"${principal_value}", font_size=20).next_to(simple_dots[0], UP)
        self.play(Write(starting_dot_label))
        self.wait(0.5)
        
        # Show simple interest line
        self.play(
            Create(simple_line),
            FadeIn(simple_dots[1:]),
            run_time=2
        )
        self.play(Write(simple_label))
        
        # Now show compound interest curve
        self.play(
            Create(compound_graph),
            FadeIn(compound_dots),
            run_time=2
        )
        self.play(Write(compound_label))
        self.wait(1)
        
        # Highlight the difference
        final_simple = simple_amounts[-1]
        final_compound = compound_amounts[-1]
        
        simple_final_label = Text(f"${final_simple:.2f}", font_size=20, color=BLUE)
        simple_final_label.next_to(simple_dots[-1], UP)
        
        compound_final_label = Text(f"${final_compound:.2f}", font_size=20, color=GREEN)
        compound_final_label.next_to(compound_dots[-1], UP)
        
        self.play(
            Write(simple_final_label),
            Write(compound_final_label)
        )
        
        difference = final_compound - final_simple
        diff_text = Text(f"Difference: ${difference:.2f}", font_size=24, color=YELLOW)
        diff_text.to_edge(RIGHT).shift(UP)
        
        self.play(Write(diff_text))
        self.wait(1)
        
        # Breakdown of compound interest calculation
        self.play(
            FadeOut(diff_text),
            FadeOut(simple_final_label),
            FadeOut(compound_final_label),
            FadeOut(simple_dots),
            FadeOut(simple_line),
            FadeOut(simple_label),
            FadeOut(compound_dots),
            FadeOut(compound_graph),
            FadeOut(compound_label),
            FadeOut(starting_dot_label)
        )
        
        # Show calculation for each year
        calc_group = VGroup()
        for year in range(years + 1):
            if year == 0:
                formula_text = MathTex(f"\\text{{Year {year}}}: \\${principal_value:.2f}", font_size=28)
            else:
                previous = compound_amounts[year-1]
                current = compound_amounts[year]
                interest_earned = current - previous
                
                formula_text = MathTex(
                    f"\\text{{Year {year}}}: \\${previous:.2f} \\times (1 + {interest_rate}) = \\${current:.2f}",
                    font_size=28
                )
                
                interest_text = MathTex(
                    f"\\text{{Interest earned: }}\\${interest_earned:.2f}",
                    font_size=24,
                    color=YELLOW
                )
                interest_text.next_to(formula_text, RIGHT, buff=0.5)
                
                formula_text = VGroup(formula_text, interest_text)
            
            calc_group.add(formula_text)
        
        calc_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        calc_group.next_to(example_text, DOWN, buff=0.75)
        
        for item in calc_group:
            self.play(Write(item))
            self.wait(0.5)
        
        # Final formula
        final_formula = MathTex(
            r"\text{Compound Interest} &= P [(1 + i)^n - 1] \\",
            r"&= 1000 [(1 + 0.1)^5 - 1] \\",
            r"&= 1000 [1.61051 - 1] \\",
            r"&= 1000 \times 0.61051 \\",
            r"&= 610.51",
            font_size=32
        )
        
        self.play(
            FadeOut(calc_group),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(example_text)
        )
        
        final_formula.next_to(title, DOWN, buff=1)
        
        self.play(Write(final_formula), run_time=3)
        self.wait(1)
        
        # Conclusion
        conclusion = Text("The power of compound interest grows over time!", font_size=32, color=YELLOW)
        conclusion.next_to(final_formula, DOWN, buff=1)
        
        self.play(Write(conclusion))
        self.wait(2)
        
        self.play(
            FadeOut(title),
            FadeOut(final_formula),
            FadeOut(conclusion)
        )
        
        # Final emphasis on the formula
        final_display = VGroup(
            Text("Remember:", font_size=36),
            MathTex(r"\text{Compound Interest} = P [(1 + i)^n - 1]", font_size=48)
        ).arrange(DOWN, buff=0.75)
        
        self.play(Write(final_display))
        self.wait(2)
        
        self.play(FadeOut(final_display))
        self.wait(1)