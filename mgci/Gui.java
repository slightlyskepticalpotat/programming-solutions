import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class Gui extends JFrame implements ActionListener {
    JButton b;
    JButton b2;
    private int clicks = 0;

    public Gui() {
        this.setTitle("First Frame");
        this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        this.setSize(200, 200);
        this.setVisible(true);

        b = new JButton("click me!");
        b.addActionListener(this);
        b2 = new JButton("click me again!");
        Container c = getContentPane();
        c.setLayout(new FlowLayout());
        // c.setLayout(new BorderLayout());
        // four directions and centre
        // c.add(b, BorderLayout.WEST);

        // c.setLayout(new GridLayout(2, 2, x, y));
        // x, y control spacing between buttons
        // c.add(b);

        // c.setLayout(null);
        // b.setSize(x, y);
        // b.setLocation(x, y);
        c.add(b);
        c.add(b2);
    }

    public static void main(String[] args) {
        new Gui();
    }

    public void paint(Graphics g) {
        super.paint(g);
        g.setFont(new Font("Comic Sans MS", Font.PLAIN, 20));
        g.drawString("JFrame creates Frames!", 500, 500);
    }

    public void actionPerformed(ActionEvent e) {
        if (clicks % 2 == 0) {
            getContentPane().setBackground(Color.BLUE);
        } else {
            getContentPane().setBackground(new Color(102, 0, 153));
        }
        repaint();
        clicks += 1;
        System.out.println(clicks);
    }
}
// todo actionlistener