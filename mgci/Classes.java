class Person {
    private String firstName;
    private String lastName;
    private String address;
    private int phone;
    private int age;

    public Person(String firstN, String lastN) {
        firstName = firstN;
        lastName = lastN;
    }

    public Person(String firstN, String lastN, String a, int p, int age) {
        firstName = firstN;
        lastName = lastN;
        address = a;
        phone = p;
        this.age = age;
    }

    public void setName(String firstN, String lastN) {
        firstName = firstN;
        lastName = lastN;
    }

    public void setContact(String address, int phone) {
        this.address = address;
        this.phone = phone;
    }

    public void setAge(int a) {
        age = a;
    }

    public static String getSchool() {
        return "Marc Garneau CI";
    }

    public String getName() {
        return firstName + " " + lastName;
    }

    public String getContact() {
        return address + " " + phone;
    }

    public int getAge() {
        return age;
    }

    public String toString() {
        return firstName + " " + lastName + " " + address + " " + phone + " " + age;
    }
}

class Student extends Person {
    private String[][] coursesGrades = new String[4][2];
    private int studentNumber;

    public Student(String[] courses, int n, String firstN, String lastN) {
        super(firstN, lastN);
        for (int i = 0; i < courses.length; i++) {
            coursesGrades[i][0] = courses[i];
        }
        studentNumber = n;
    }

    public void setNumber(int n) {
        studentNumber = n;
    }

    public void setCourseGrade(double g, String course) {
        for (int i = 0; i < 4; i++) {
            if (coursesGrades[i][0] != null) {
                if (coursesGrades[i][0].equals(course)) {
                    coursesGrades[i][1] = g + "";
                }
            }
        }
    }

    public int getNumber() {
        return studentNumber;
    }

    public double getAverage() {
        double total = 0;
        for (int i = 0; i < this.numOfCourses(); i++) {
            total += Double.parseDouble(coursesGrades[i][1]);
        }
        return total / (double) this.numOfCourses();
    }

    public String toString() {
        return super.toString() + " " + studentNumber + " " + coursesGrades.toString();
    }

    private int numOfCourses() {
        int courses = 0;
        for (int i = 0; i < 4; i++) {
            if (coursesGrades[i][0] != null) {
                courses += 1;
            }
        }
        return courses;
    }
}

class Teacher extends Person {
    private int employeeNumber;
    private int seniority;

    public Teacher(int eNum, String firstN, String lastN) {
        super(firstN, lastN);
        employeeNumber = eNum;
    }

    public void setSeniority(int s) {
        seniority = s;
    }

    public void setNum(int n) {
        employeeNumber = n;
    }

    public int getSeniority() {
        return seniority;
    }

    public int getNum() {
        return employeeNumber;
    }

    public boolean isSenior(Teacher t) {
        if (this.seniority > t.seniority) {
            return true;
        }
        return false;
    }

    public String toString() {
        return super.toString() + " " + employeeNumber + " " + seniority;
    }
}

public class Classes {
    public static void main(String[] args) {
        String[] courses = {"ics", "comp eng"};
        Student s = new Student(courses, 1, "John", "Doe");
        s.setCourseGrade(100.0, "ics");
        s.setCourseGrade(99.0, "comp eng");
        System.out.println(s.getAverage());

        Teacher t1 = new Teacher(1, "Teacher", "One");
        Teacher t2 = new Teacher(2,"Teacher", "Two");
        t1.setSeniority(1);
        t2.setSeniority(2);
        if (t1.isSenior(t2)) {
            t1.setNum(111111);
            t2.setNum(111112);
        } else {
            t2.setNum(111111);
            t1.setNum(111112);
        }

        System.out.println(s);
        System.out.println(t1);
        System.out.println(t2);
    }
}