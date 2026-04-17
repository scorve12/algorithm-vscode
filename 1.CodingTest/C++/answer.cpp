#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <string>

using namespace std;

#define AUTOMATIC_ERROR_CHECK false

class Person
{
    string name;
    string passwd;     // 문제 8: 비번 추가
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
    // 문제 3: 위임 생성자 (클래스 선언부에서 인라인으로 처리)
    Person() : Person("") {}
    Person(const string name) : Person(name, 0, 0.0, false, "") {}

    Person(const string name, int id, double weight, bool married, const char *address)
        : name(name), passwd{}, id{id}, weight{weight}, married{married} {
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

    void setName(const string name)   { this->name = name; }
    void setPasswd(const string passwd) { this->passwd = passwd; }  // 문제 8
    void setId(int id)                { this->id = id; }
    void setWeight(double weight)     { this->weight = weight; }
    void setMarried(bool married)     { this->married = married; }
    void setAddress(const char* address) { strcpy(this->address, address); }

    string getName()        { return name; }
    string getPasswd()      { return passwd; }  // 문제 8
    int    getId()          { return id; }
    double getWeight()      { return weight; }
    bool   getMarried()     { return married; }
    const char* getAddress(){ return address; }

    void input(istream* pin)  { inputMembers(pin); }
    void print(ostream* pout) { printMembers(pout); }
    void println()            { print(&cout); cout << endl; }

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
string line;   // 문제 8: getNext/getNextLine에서 사용

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

// 문제 8: 단어 단위 입력
string getNext(const string msg) {
    cout << msg;
    cin >> line;
    if (echo_input) cout << line << endl;
    getline(cin, emptyLine); 
    return line;
}


string getNextLine(const string msg) {
    cout << msg;
    getline(cin, line);
    if (echo_input) cout << line << endl;
    return line;
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

}  // namespace UI

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

    // 문제 9: 비밀번호 변경
    void changePasswd() {
        string newPasswd = UI::getNext("New password: ");
        pUser->setPasswd(newPasswd);
        cout << "Password changed" << endl;
    }

    void run() {
        using CU = CurrentUser;  // 문제 9: 코딩 길이 단축
        using func_t = void (CurrentUser::*)();
        func_t func_arr[] = {
            nullptr, &CU::display, &CU::getter,
            &CU::setter, &CU::set,
            &CU::whatAreYouDoing,
            &CU::isSame, &CU::inputPerson,
            &CU::changePasswd,   // 문제 9
        };

        int menuCount = sizeof(func_arr) / sizeof(func_arr[0]);

        // 문제 9: 메뉴 문자열 업데이트
        string menuStr =
            "+++++++++++++++++++++ Current User Menu ++++++++++++++++++++++++\n"
            "+ 0.Logout 1.Display 2.Getter 3.Setter 4.Set 5.WhatAreYouDoing +\n"
            "+ 6.IsSame 7.InputPerson 8.ChangePasswd(4_2)                   +\n"
            "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n";


        while (true) {
            int menuItem = UI::selectMenu(menuStr, menuCount);
            if (menuItem == 0) return;
            (this->*func_arr[menuItem])();
        }
    }
};

/******************************************************************************/

// 문제 1, 2, 4, 7: VectorPerson 클래스
class VectorPerson
{
    static const int DEFAULT_SIZE = 10;

    Person **pVector;
    int count;
    int allocSize;

    void extend_capacity();  // 문제 7

public:
    // 문제 2: 위임 생성자
    VectorPerson() : VectorPerson(DEFAULT_SIZE) {}

    VectorPerson(int capacity) : count(0), allocSize(capacity) {
        cout << "VectorPerson::VectorPerson(" << allocSize << ")" << endl;
        pVector = new Person*[allocSize];
    }

    // 문제 2: 소멸자 - 배열 반납
    ~VectorPerson() {
        delete[] pVector;
        cout << "VectorPerson::~VectorPerson(): pVector deleted" << endl;
    }

    // 문제 1: 단순 멤버 함수 구현
    Person* at(int index) const { return pVector[index]; }
    int     capacity()    const { return allocSize; }
    void    clear()             { count = 0; }
    bool    empty()       const { return count == 0; }
    int     size()        const { return count; }

    void push_back(Person* p);  // 문제 4, 7
};

// 문제 4, 7: push_back - 가득 찼으면 용량 확장 후 삽입
void VectorPerson::push_back(Person* p) {
    if (count >= allocSize)
        extend_capacity();
    pVector[count++] = p;
}

// 문제 7: 배열 크기를 두 배로 확장
void VectorPerson::extend_capacity() {
    Person **saved_persons = pVector;
    allocSize *= 2;
    pVector = new Person*[allocSize];
    for (int i = 0; i < count; ++i)
        pVector[i] = saved_persons[i];
    delete[] saved_persons;
    cout << "VectorPerson: capacity extended to " << allocSize << endl;
}

/******************************************************************************/

// 문제 6: Factory 클래스
class Factory
{
    Person* checkInputFormatError(istream* in, Person* p) {
        if (UI::checkDataFormatError(in)) {
            delete p;
            return nullptr;
        }
        if (UI::echo_input) p->println();
        return p;
    }

public:
    Person* inputPerson(istream* in) {
        Person* p = new Person();
        p->input(in);
        return checkInputFormatError(in, p);
    }
};

/******************************************************************************/

// 문제 4~8: PersonManager 클래스
class PersonManager
{
    VectorPerson persons;
    Factory factory;  // 문제 6

    void deleteElemets();
    void printNotice(const string preMessage, const string postMessage);
    Person* findByName(const string name);

public:
    PersonManager(Person* array[], int len);
    ~PersonManager();
    void display();
    void append();
    void clear();
    void login();
    void run();
};

// 문제 4: array[]의 각 객체를 복사하여 동적 생성 후 persons에 삽입
PersonManager::PersonManager(Person* array[], int len) {
    cout << "PersonManager::PersonManager(array[], len)" << endl;
    for (int i = 0; i < len; ++i) {
        Person *s = array[i];
        Person *p = new Person(s->getName(), s->getId(), s->getWeight(),
                               s->getMarried(), s->getAddress());
        persons.push_back(p);
    }
    display();
}

PersonManager::~PersonManager() {
    deleteElemets();
    display();
}

// 문제 5: persons에 저장된 모든 객체 메모리 반납 후 count 초기화
void PersonManager::deleteElemets() {
    for (int i = 0; i < persons.size(); ++i) {
        delete persons.at(i);
    }
    persons.clear();
}

void PersonManager::display() {
    int count = persons.size();
    cout << "display(): count " << count << endl;
    for (int i = 0; i < count; ++i) {
        cout << "[" << i << "] ";
        persons.at(i)->println();
    }
    cout << "empty():" << persons.empty() << ", size():" << persons.size()
         << ", capacity():" << persons.capacity() << endl;
}

// 문제 6
void PersonManager::printNotice(const string preMessage, const string postMessage) {
    cout << preMessage;
    cout << " [person information] " << postMessage << endl;
}

// 문제 6: 추가할 인원 수 입력받고 factory로 Person 생성 후 삽입
void PersonManager::append() {
    int count = UI::getPositiveInt("The number of persons to append? ");
    printNotice("Input " + to_string(count), ":");
    for (int i = 0; i < count; ++i) {
        Person* p = factory.inputPerson(&cin);
        if (p) persons.push_back(p);
    }
    display();
}

void PersonManager::clear() {
    deleteElemets();
    display();
}

// 문제 8: 이름으로 Person 검색
Person* PersonManager::findByName(const string name) {
    for (int i = 0; i < persons.size(); ++i) {
        if (persons.at(i)->getName() == name)
            return persons.at(i);
    }
    cout << name + ": NOT found" << endl;
    return nullptr;
}

// 문제 8: 이름·비번 확인 후 CurrentUser 실행
void PersonManager::login() {
    string name = UI::getNext("user name: ");
    Person* p = findByName(name);
    if (p == nullptr) return;
    string passwd = UI::getNextLine("password: ");
    if (passwd != p->getPasswd())
        cout << "WRONG password!!" << endl;
    else
        CurrentUser(p).run();
}

void PersonManager::run() {
    using func_t = void (PersonManager::*)();
    using PM = PersonManager;
    func_t func_arr[] = {
        nullptr, &PM::display, &PM::append, &PM::clear, &PM::login,
    };
    int menuCount = sizeof(func_arr) / sizeof(func_arr[0]);
    string menuStr =
        "====================== Person Management Menu ===================\n"
        "= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =\n"
        "=================================================================\n";

    while (true) {
        int menuItem = UI::selectMenu(menuStr, menuCount);
        if (menuItem == 0) return;
        (this->*func_arr[menuItem])();
    }
}

/******************************************************************************/

// 코드 추가 3: MultiManager - Person 배열 + PersonManager 조합
class MultiManager
{
    static const int personCount = 5;
    Person persons[personCount] = {
        Person("p0", 10, 70.0, false, "Gwangju Nam-gu Bongseon-dong 21"),
        Person("p1", 11, 61.1, true,  "Jong-ro 1-gil, Jongno-gu, Seoul"),
        Person("p2", 12, 52.2, false, "1001, Jungang-daero, Yeonje-gu, Busan"),
        Person("p3", 13, 83.3, true,  "100 Dunsan-ro Seo-gu Daejeon"),
        Person("p4", 14, 64.4, false, "88 Gongpyeong-ro, Jung-gu, Daegu"),
    };

    static const int allPersonCount = personCount;
    Person* allPersons[allPersonCount] = {
        &persons[0], &persons[1], &persons[2], &persons[3], &persons[4],
    };

    PersonManager personMng { allPersons, allPersonCount };

public:
    void run() {
        cout << "PersonManager::run() starts" << endl;
        personMng.run();
        cout << "PersonManager::run() returned" << endl;
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

/******************************************************************************/

class MainMenu
{
public:
    void run() {
        int menuCount = 3;
        // 코드 추가 4: 메뉴 문자열 변경
        string menuStr =
"******************************* Main Menu *********************************\n"
"* 0.Exit 1.PersonManager(ch3_2, 4)                                        *\n"
"* 2.Class:Object(ch3_1)                                                   *\n"
"***************************************************************************\n";

        while (true) {
            int menuItem = UI::selectMenu(menuStr, menuCount);
            if (menuItem == 0) break;

            switch(menuItem) {
            case 1: MultiManager().run(); break;  // 코드 추가 4
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
