#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <string>

using namespace std;

#define AUTOMATIC_ERROR_CHECK false

class Person
{
    string name;      // char name[20] -> string name 으로 변경
    int id;
    double weight;
    bool married;
    char address[40];

protected:
    void inputMembers(istream* pin) {
        *pin >> name >> id >> weight >> married;
        if (!(*pin)) return;
        pin->getline(address, sizeof(address), ':');
        pin->getline(address, sizeof(address), ':');
    }

    void printMembers(ostream* out) {
        *out << name << " "
             << id << " "
             << weight << " "
             << married << " :"
             << address << ":";
    }

public:
    Person(): name{}, id{}, weight{}, married{}, address{} {
        cout << "Person::Person():"; println();
    }

    Person(const string name): name(name), id{}, weight{}, married{}, address{} {
        cout << "Person::Person(\"" << name << "\"):"; println();
    }

    Person(const string name, int id, double weight, bool married, const char *address)
        : name(name), id{id}, weight{weight}, married{married} {
        setAddress(address);
        cout << "Person::Person(...):"; println();
    }

    ~Person() {
        cout << "Person::~Person():"; println();
    }

    void set(const string name, int id, double weight, bool married, const char *address) {
        this->name = name;
        this->id = id;
        this->weight = weight;
        this->married = married;
        setAddress(address);
    }

    void setName(const string name) { this->name = name; }
    void setId(int id) { this->id = id; }
    void setWeight(double weight) { this->weight = weight; }
    void setMarried(bool married) { this->married = married; }
    void setAddress(const char* address) { strcpy(this->address, address); }

    string getName() { return name; }
    int getId() { return id; }
    double getWeight() { return weight; }
    bool getMarried() { return married; }
    const char* getAddress() { return address; }

    void input(istream* pin) { inputMembers(pin); }
    void print(ostream* pout) { printMembers(pout); }
    void println() { print(&cout); cout << endl; }

    void whatAreYouDoing() {
        cout << name << " is taking a rest." << endl;
    }

    bool isSame(const string name, int id) {
        return (this->name == name && this->id == id);
    }
};

namespace UI {

bool echo_input = false;
string emptyLine;

bool checkInputError(istream* pin, const string msg) {
    if (!(*pin)) {
        cout << msg;
        pin->clear();
        getline(*pin, emptyLine);
        return true;
    }
    return false;
}

bool checkDataFormatError(istream* pin) {
    return checkInputError(pin, "Input-data format MISMATCHED\n");
}

bool inputPerson(Person* p) {
    cout << "input person information:" << endl;
    p->input(&cin);
    if (checkDataFormatError(&cin)) return false;
    if (echo_input) p->println();
    return true;
}

int getInt(const string msg) {
    for (int value; true;) {
        cout << msg;
        cin >> value;
        if (echo_input) cout << value << endl;
        if (checkInputError(&cin, "Input an INTEGER.\n"))
            continue;
        getline(cin, emptyLine);
        return value;
    }
}

int getPositiveInt(const string msg) {
    int value;
    while ((value = getInt(msg)) < 0)
        cout << "Input a positive INTEGER." << endl;
    return value;
}

int getIndex(const string msg, int size) {
    while (true) {
        int index = getPositiveInt(msg);
        if (0 <= index && index < size) return index;
        cout << index << ": OUT of selection range(0 ~ "
             << size-1 << ")" << endl;
    }
}

int selectMenu(const string menuStr, int menuItemCount) {
    cout << endl << menuStr;
    return getIndex("Menu item number? ", menuItemCount);
}

}

/******************************************************************************/

class CurrentUser
{
    Person* pUser;

public:
    CurrentUser(Person* pUser): pUser(pUser) {}

    void display() {
        pUser->println();
    }

    void getter() {
        cout << "name:" << pUser->getName()
             << ", id:" << pUser->getId()
             << ", weight:" << pUser->getWeight()
             << ", married:" << pUser->getMarried()
             << ", address:" << pUser->getAddress() << endl;
    }

    void setter() {
        Person* pp = new Person("pp");
        pp->setName(pp->getName());
        pp->setId(pUser->getId());
        pp->setWeight(pUser->getWeight());
        pp->setMarried(pUser->getMarried());
        pp->setAddress(pUser->getAddress());
        cout << "pp->setMembers():"; pp->println();
        delete pp;
    }

    void set() {
        Person* pp = new Person("pp");
        pp->set(pp->getName(), pUser->getId(), pUser->getWeight(),
               !pUser->getMarried(), pUser->getAddress());
        cout << "pp->set():"; pp->println();
        delete pp;
    }

    void whatAreYouDoing() {
        pUser->whatAreYouDoing();
    }

    void isSame() {
        pUser->println();
        cout << "isSame(\"user\", 1): "
             << pUser->isSame("user", 1) << endl;
    }

    void inputPerson() {
        if (UI::inputPerson(pUser))
            display();
    }

    void run() {
        using func_t = void (CurrentUser::*)();
        func_t func_arr[] = {
            nullptr, &CurrentUser::display, &CurrentUser::getter,
            &CurrentUser::setter, &CurrentUser::set,
            &CurrentUser::whatAreYouDoing,
            &CurrentUser::isSame, &CurrentUser::inputPerson,
        };

        int menuCount = sizeof(func_arr) / sizeof(func_arr[0]);

        string menuStr =
            "+++++++++++++++++++++ Current User Menu ++++++++++++++++++++++++\n"
            "+ 0.Logout 1.Display 2.Getter 3.Setter 4.Set 5.WhatAreYouDoing +\n"
            "+ 6.IsSame 7.InputPerson                                       +\n"
            "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n";

        while (true) {
            int menuItem = UI::selectMenu(menuStr, menuCount);
            if (menuItem == 0) return;
            (this->*func_arr[menuItem])();
        }
    }
};

/******************************************************************************/

class ClassAndObject
{
public:
    void run() {
        cout << "CH3_1 메뉴는 생략됨" << endl;
    }
};

class MultiManager
{
    Person person {"p0", 0, 70.0, false, "Gwangju Nam-gu Bongseon-dong 21"};

public:
    void currentUser() {
        CurrentUser(&person).run();
    }
};

/******************************************************************************/

class MainMenu
{
public:
    void run() {
        int menuCount = 3;
        string menuStr =
"******************************* Main Menu *********************************\n"
"* 0.Exit 1.CurrentUser(ch3_2, 4_1)                                        *\n"
"* 2.Class:Object(ch3_1)                                                   *\n"
"***************************************************************************\n";

        while (true) {
            int menuItem = UI::selectMenu(menuStr, menuCount);
            if (menuItem == 0) break;

            switch(menuItem) {
            case 1: MultiManager().currentUser(); break;
            case 2: ClassAndObject().run(); break;
            }
        }
        cout << "Good bye!!" << endl;
    }
};

/******************************************************************************/

void run() {
    MainMenu().run();
}

int main() {
    cout << boolalpha;
    cin >> boolalpha;
    run();
}