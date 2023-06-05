import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class FatCalc extends JFrame implements ActionListener {
    JTextField tf = new JTextField(8);
    JTextField tf2 = new JTextField(8);
    JTextField tf3 = new JTextField(8);
    int cals, fatg;
    double percent;
    JButton b;

    private void calcPercent() {
        percent = ((fatg * 9.0) / cals) * 100.0;
    }

    public FatCalc (){
        this.setTitle("Calories From Fat");
        this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        this.setSize(280, 200);
        this.setVisible(true);

        JLabel title = new JLabel("% of Calories From Fat");
        JLabel title2 = new JLabel("Grams of Fat:");
        JLabel title3 = new JLabel("Total Calories:");
        JLabel title4 = new JLabel("% of Calories From Fat:");
        Container c = getContentPane();
        c.setLayout(new FlowLayout());
        c.add(title);
        c.add(title2);
        c.add(tf);
        c.add(title3);
        c.add(tf2);
        c.add(title4);
        c.add(tf3);
        tf3.setEditable(false);
        b = new JButton("CALCULATE");
        b.addActionListener(this);

        JButton reset = new JButton(new AbstractAction("reset") {
            @Override
            public void actionPerformed(ActionEvent e) {
                tf.setText("");
                tf2.setText("");
                tf3.setText("");
                repaint();
            }
        });
        c.add(b);
        c.add(reset);
    }

    public static void main(String[] args) {
        new FatCalc();
    }

    public void paint(Graphics g) {
        super.paint(g);
    }

    public void actionPerformed(ActionEvent e) {
        fatg = Integer.parseInt(tf.getText());
        cals = Integer.parseInt(tf2.getText());

        calcPercent();
        tf3.setText(percent + " ");
        repaint();
    }
}
