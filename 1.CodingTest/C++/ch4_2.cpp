[4장 문제-2]

//----------------------------------------------------------------------------
// 아래 문제를 해결하는 도중 출력이 잘못되었거나 문제 설명과 출력이 일치하지 않거나 오타가 있거나 등등
// 조금이라도 문제에 이상한 것이 있으면 주저하지 말고 mskang@chosun.ac.kr로 알려 주시기 바랍니다.
//----------------------------------------------------------------------------

/******************************************************************************
 * 프로젝트 및 소스파일 생성
 ******************************************************************************/
// 기존의 과제를 수행했던 이클립스의 작업공간에서 새로운 프로젝트 CH4_2를 만들고 
// 그 밑에 src 풀더를 만든 후 src 폴더 밑에 ch4_2.cpp 소스파일을 만들어라.

/******************************************************************************
 * 코드 추가 1
 ******************************************************************************/
// 1) 기존에 작성했던 ch4_1.cpp의 내용을 모두 복사해서 ch4_2.cpp에 삽입하라.
// 2) 프로그램의 맨 앞쪽 주석 부분의 "Author: " 행 다음의 내용을 아래 *로 시작하는 행들로 교체하라.
//----------------------------------------------------------------------------
 *
 *  + UI::getNext(), UI::getNextLine() 추가
 *  + Person::passwd, getPasswd(), setPasswd() 추가
 *  + VectorPerson 클래스 추가: 객체 포인터 배열의 생성 및 소멸
 *  + PersonManager 클래스 추가: 객체 배열의 복사, 객체의 동적 생성 및 소멸
 *  + MultiManager 클래스: 객체 배열로 변경
 */

/******************************************************************************
 * 코드 추가 2
 ******************************************************************************/
// 아래 코드를 class CurrentUser와 class MultiManager 사이에 삽입하라.
//----------------------------------------------------------------------------

/******************************************************************************
 * ch4_2: VectorPerson class
 ******************************************************************************/
// VectorPerson는 n개의 Person * 포인터를 pVector[] 배열에 담아 관리하는 클래스이다.
// 필요에 따라 포인터를 삽입, 삭제, 추가 등을 할 수 있다.
// 삽입하는 포인터 개수가 점점 많아지면 pVector[] 배열을 위한 메모리를 자동 확장하기도 한다.

class VectorPerson
{
    static const int DEFAULT_SIZE = 10; // pVector의 디폴트 배열 원소 개수

    Person **pVector; // Person *pVector[]; Person에 대한 포인터들의 배열, 배열에 저장될 값이 Person *이다.
    int count;        // pVector 배열에 현재 삽입된 객체 포인터의 개수
    int allocSize;    // 할당 받의 pVector의 총 배열 원소의 개수

    void extend_capacity(); /* TODO 문제 [7] */

public:
    VectorPerson() {  /* TODO 문제 [2]: 위임 생성자로 변환 */
        allocSize = DEFAULT_SIZE;
        count = 0;
        cout << "VectorPerson::VectorPerson(" << allocSize << ")" << endl;
        pVector = new Person*[allocSize]; // 객체 포인터들의 배열을 위한 동적 메모리 할당
    }
    VectorPerson(int capacity);
    ~VectorPerson();

    // 아래 긱 함수이름 뒤의 const는 그 함수가 클래스 멤버 변수들을 수정하지 않고 읽기만 한다는 의미임
    // pVector[index]의 포인터 값을 반환 
    Person* at(int index) const { /* TODO 문제 [1] */ return nullptr; }

    // 할당 받의 pVector의 총 배열 원소의 개수를 반환
    int     capacity()    const { /* TODO 문제 [1] */ return 0; }

    // pVector 배열에 현재 삽입된 객체 포인터의 개수를 0으로 설정
    void    clear()             { /* TODO 문제 [1] */ }

    // 현재 삽입된 객체 포인터가 하나도 없으면 true, 있으면 false
    bool    empty()       const { /* TODO 문제 [1] */ return true; }

    // 현재 삽입된 객체 포인터의 개수를 반환
    int     size()        const { /* TODO 문제 [1] */ return 0; }

    // pVector 배열에 마지막 삽입된 원소 뒤에 새로운 원소 p를 삽입하고 현재 삽입된 객체 개수를 증가
    void    push_back(Person* p); /* TODO 문제 [4, 7] */
};

// capacity는 할당해야 할 배열 원소의 개수
VectorPerson::VectorPerson(int capacity) /* : TODO 문제 [2]: 멤버 초기화 */ {
    // allocSize = capacity, count = 0; 초기화를 위 함수 서두(위 /* */ 주석 사이)에서 할 것
    // 함수 서두에서 초기화하는 방법은 Person 클래스 참고할 것
    cout << "VectorPerson::VectorPerson(" << allocSize << ")" << endl;
    pVector = new Person*[allocSize]; // Person* 들의 배열을 위한 동적 메모리 할당
}

VectorPerson::~VectorPerson() {
    /* TODO 문제 [2]: 동적으로 할당된 배열 pVector 반납: pVector가 배열임을 명심하라. */
    // cout << "VectorPerson::~VectorPerson(): pVector deleted" << endl;
}

/******************************************************************************
 * ch4_2: PersonManager class
 ******************************************************************************/

class PersonManager
{
    VectorPerson persons;

    void deleteElemets();
    void printNotice(const string preMessage, const string postMessage);
    Person* findByName(const string name);

public:
    PersonManager(Person* array[], int len); // 6장에서 default 매개변수 설정
    ~PersonManager();
    void display();
    void append();
    void clear();
    void login();
    void run();
};

PersonManager::PersonManager(Person* array[], int len) {
    cout << "PersonManager::PersonManager(array[], len)" << endl;
    /* TODO 문제 [4] */
    display();
}

PersonManager::~PersonManager() {
    deleteElemets();
    display();
}

void PersonManager::deleteElemets() {
    /* TODO 문제 [5] */
}

void PersonManager::display() { // Menu item 1
    int count = persons.size();
    cout << "display(): count " << count << endl;
    for (int i = 0; i < count; ++i) {
        cout << "[" << i << "] ";
        persons.at(i)->println();
    }
    cout << "empty():" << persons.empty() << ", size():" << persons.size()
         << ", capacity():" << persons.capacity() << endl;
}

void PersonManager::append() { /* TODO 문제 [6] */ } // Menu item 2

void PersonManager::clear() { // Menu item 3
    deleteElemets();
    display();
}
void PersonManager::login() { // Menu item 4 
    /* TODO 문제 [8] */ 
}

void PersonManager::run() {
    using func_t = void (PersonManager::*)();
    using PM = PersonManager; // 코딩 길이를 줄이기 위해
    func_t func_arr[] = {
        nullptr, &PM::display, &PM::append, &PM::clear, &PM::login,
    };
    int menuCount = sizeof(func_arr) / sizeof(func_arr[0]); // func_arr[] 길이
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

/******************************************************************************
 * 코드 추가 3
 ******************************************************************************/
// 기존의 class MultiManager를 아래 코드로 대체하라.
//----------------------------------------------------------------------------

/******************************************************************************
 * ch3_2, 4_1, 4_2: MultiManager class
 ******************************************************************************/
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
    // new를 이용해 동적으로 할당할 경우 소멸자 함수를 만들어 거기서 delete 해 주어야 함

    static const int allPersonCount = personCount;
    Person* allPersons[allPersonCount] = {
        &persons[0], &persons[1], &persons[2], &persons[3], &persons[4],
    };

    PersonManager personMng { allPersons, allPersonCount };
    // 위 문장은 PersonManager personMng(allPersons, allPersonCount);와 동일함

public:
    void run() {
        cout << "PersonManager::run() starts" << endl;
        personMng.run();
        cout << "PersonManager::run() returned" << endl;
    }
}; // ch3_2, 4_1, 4_2: MultiManager class


/******************************************************************************
 * 코드 추가 4
 ******************************************************************************/
// MainMenu::run() 코드 중 상응하는 부분을 아래 코드로 대체하라.
//----------------------------------------------------------------------------

        string menuStr =
"******************************* Main Menu *********************************\n"
"* 0.Exit 1.PersonManager(ch3_2, 4)                                        *\n"
"* 2.Class:Object(ch3_1)                                                   *\n"
"***************************************************************************\n";
            ...
            case 1: MultiManager().run();             break;


===============================================================================
== 초기 프로그램 실행 결과
== 위 프로그램을 실행시키면 아래처럼 출력되어야 한다.
=============================================================================== 
******************************* Main Menu *********************************
* 0.Exit 1.PersonManager(ch3_2, 4)                                        *
* 2.Class:Object(ch3_1)                                                   *
***************************************************************************
Menu item number? 1   // 아래는 MultiManager::persons[]의 배열 객체 생성임
Person::Person(...):p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:
Person::Person(...):p1 11 61.1 true :Jong-ro 1-gil, Jongno-gu, Seoul:
Person::Person(...):p2 12 52.2 false :1001, Jungang-daero, Yeonje-gu, Busan:
Person::Person(...):p3 13 83.3 true :100 Dunsan-ro Seo-gu Daejeon:
Person::Person(...):p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
VectorPerson::VectorPerson(10)
PersonManager::PersonManager(array[], len)
display(): count 0
empty():true, size():0, capacity():0
PersonManager::run() starts

====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 1
display(): count 0
empty():true, size():0, capacity():0

...
Menu item number? 0
PersonManager::run() returned
display(): count 0
empty():true, size():0, capacity():0    // 아래는 MultiManager::persons[]의 배열 객체 소멸임
Person::~Person():p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
Person::~Person():p3 13 83.3 true :100 Dunsan-ro Seo-gu Daejeon:
Person::~Person():p2 12 52.2 false :1001, Jungang-daero, Yeonje-gu, Busan:
Person::~Person():p1 11 61.1 true :Jong-ro 1-gil, Jongno-gu, Seoul:
Person::~Person():p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:


/******************************************************************************
 * 문제 1
 ******************************************************************************/
// class VectorPerson의 at(), capacity(), empty(), size(), clear()
// 멤버 함수들의 위쪽에 있는 주석문을 참고하여 해당 함수들을 구현하라.

===============================================================================
== 문제 1 실행 결과
=============================================================================== 
...
====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 1
display(): count 0
empty():true, size():0, capacity():10


/******************************************************************************
 * 문제 2
 ******************************************************************************/
// 1) VectorPerson::VectorPerson()을 [교재 예제 3-4]를 참조하여 위임 생성자로 만들어라. 
//    즉, 함수 본체 내용을 모두 삭제하고 함수 서두(: 와 { 사이)에서 매개변수가 있는 생성자 
//    VectorPerson(int capacity)를 호출하라. 

// 2) VectorPerson::VectorPerson(int capacity)의 함수 서두에서 
//    count, allocSize 멤버들을 초기화 하라. 함수 서두에서 초기화하는 방법은
//    Person::Person(const string name, int id, ...) 구현 함수를 참조하라.

// 3) VectorPerson::~VectorPerson()의 주석을 참조하여 pVector를 반납하는 코드를 삽입하라.
//    또한 // cout << ...; 문장의 주석을 풀어라.

===============================================================================
== 문제 2 실행 결과
=============================================================================== 
...
====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 0
PersonManager::run() returned
display(): count 0
empty():true, size():0, capacity():10
VectorPerson::~VectorPerson(): pVector deleted     // ~VectorPerson()에서 출력
Person::~Person():p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
...
Person::~Person():p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:


/******************************************************************************
 * 문제 3
 ******************************************************************************/
// 1) Person::Person()을 [교재 예제 3-4]를 참조하여 위임 생성자로 만들어라. 
//    즉, 타겟 생성자로 Person(const string name) 호출하라. 호출 시 name은 ""로 설정하라.

// 2) Person::Person(const string name)을 [교재 예제 3-4]를 참조하여 위임 생성자로 만들어라. 
//    즉, 타겟 생성자로 Person(const string name, int id, ...)을 호출하라. 
//    호출 시 address는 ""로 설정하라.

// 3) Person::Person(), Person::Person(const string name)의 경우
//    클래스 구현부에서 구현했던 이들 함수들을 모두 삭제하고  
//    클래스 선언부 내에서 위임 생성자들이 바로 바로 타겟 생성자를 호출하도록 하라.  

===============================================================================
== 문제 3 실행 결과
=============================================================================== 
******************************* Main Menu *********************************
* 0.Exit 1.PersonManager(ch3_2, 4)                                        *
* 2.Class:Object(ch3_1)                                                   *
***************************************************************************
Menu item number? 2

+++++++++++ Person Class And Object Menu ++++++++++++
+ 0.Exit 1.DefualConstructor 2.Constructor          +
...
Menu item number? 2 // 아래에서 모두 타겟 생성자 Person::Person(...)로 출력됨에 유의하라.
Person::Person(...): 0 0 false ::
Person::Person(...):ps2 0 0 false ::
Person::Person(...):ps3 3 70.3 true :ps3 address:
Person::~Person():ps3 3 70.3 true :ps3 address:
Person::~Person():ps2 0 0 false ::
Person::~Person(): 0 0 false ::


/******************************************************************************
 * 문제 4
 ******************************************************************************/
// VectorPerson::push_back(Person* p) 함수를 클래스 외부에서 구현하라.
// 이 함수는 마지막으로 삽입했던 pVector[] 위치의 그 다음번 위치에 p를 삽입하고 (즉, 맨 뒤에 삽입)
// 삽입된 객체 포인터 개수를 1 증가시킨다.

// PersonManager::PersonManager(Person* array[], int len)에서 array[]에 저장된
// 각각의 객체를 복사하여 새로운 객체를 생성한 후 이를 VectorPerson persons에 삽입하라.
// 즉, 구현시 for문을 이용하여 각각의 array[i]에 대해
//     Person *s = array[i]; 한 후 
//     새로운 Person 객체를 동적으로 할당하여 생성하되 *s 객체 값으로 초기화하라. 
//         객체를 생성할 때 Person(const string name, int id, ...) 생성자를 이용하되 
//         생성자 인자로는 s가 포인터하는 객체의 각 멤버(s->getName(), s->getId() 등등)를 
//         순서적으로 넘겨 주어라. 즉, array[i]인 s가 포인터하는 객체와 동일한 멤버 값들을 가지는 
//         복사된 새로운 객체를 생성하는 것이다.   
//     그런 후 새로 생성된 Person 객체 포인터를 persons에 삽입하되 push_back()을 이용하라.

===============================================================================
== 문제 4 실행 결과
=============================================================================== 
******************************* Main Menu *********************************
* 0.Exit 1.PersonManager(ch3_2, 4)                                        *
* 2.Class:Object(ch3_1)                                                   *
***************************************************************************
Menu item number? 1   // 아래는 MultiManager::persons[]의 배열 객체 생성임
Person::Person(...):p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:
Person::Person(...):p1 11 61.1 true :Jong-ro 1-gil, Jongno-gu, Seoul:
Person::Person(...):p2 12 52.2 false :1001, Jungang-daero, Yeonje-gu, Busan:
Person::Person(...):p3 13 83.3 true :100 Dunsan-ro Seo-gu Daejeon:
Person::Person(...):p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
VectorPerson::VectorPerson(10)
PersonManager::PersonManager(array[], len)  // 아래는 PersonManager(array[], len)에서 동적으로 객체 복사 생성하면서 출력
Person::Person(...):p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:
Person::Person(...):p1 11 61.1 true :Jong-ro 1-gil, Jongno-gu, Seoul:
Person::Person(...):p2 12 52.2 false :1001, Jungang-daero, Yeonje-gu, Busan:
Person::Person(...):p3 13 83.3 true :100 Dunsan-ro Seo-gu Daejeon:
Person::Person(...):p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
display(): count 5    // PersonManager(array[], len)의 display()에 의해 출력
[0] p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:
[1] p1 11 61.1 true :Jong-ro 1-gil, Jongno-gu, Seoul:
[2] p2 12 52.2 false :1001, Jungang-daero, Yeonje-gu, Busan:
[3] p3 13 83.3 true :100 Dunsan-ro Seo-gu Daejeon:
[4] p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
empty():false, size():5, capacity():10
PersonManager::run() starts

====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 1
display(): count 5
[0] p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:
[1] p1 11 61.1 true :Jong-ro 1-gil, Jongno-gu, Seoul:
[2] p2 12 52.2 false :1001, Jungang-daero, Yeonje-gu, Busan:
[3] p3 13 83.3 true :100 Dunsan-ro Seo-gu Daejeon:
[4] p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
empty():false, size():5, capacity():10


/******************************************************************************
 * 문제 5
 ******************************************************************************/
// PersonManager::~PersonManager()와 PersonManager::clear()에서 하는 일은 동일하다.
// 즉, deleteElemets()를 호출하여 VectorPerson persons에 삽입된 모든 객체의 메모리를 
// 모두 반납하고 display()를 호출하여 현재 상태를 보여 주는 것이다.

// PersonManager::deleteElemets()를 구현하라. 이 함수는 
// for문을 이용하여 각 인덱스 i를 증가시키면서 (persons에 삽입된 개수 만큼 loop돔)
//     persons의 적절한 멤버 함수를 호출하여 persons의 i번째 저장된 Person 객체 포인터를 
//     얻어 온 후 그 포인터가 포인트하는 메모리를 반납시키면 된다. 
// persons의 적절한 멤버 함수를 호출하여 pVector 배열에 삽입된 객체 포인터의 개수를 0으로 설정하라.

===============================================================================
== 문제 5 실행 결과 1: PersonManager::~PersonManager() 테스트
=============================================================================== 
...
====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 0
PersonManager::run() returned  // 아래는 ~PersonManager()->deleteElemets()에서 소멸
Person::~Person():p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:
Person::~Person():p1 11 61.1 true :Jong-ro 1-gil, Jongno-gu, Seoul:
Person::~Person():p2 12 52.2 false :1001, Jungang-daero, Yeonje-gu, Busan:
Person::~Person():p3 13 83.3 true :100 Dunsan-ro Seo-gu Daejeon:
Person::~Person():p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
display(): count 0
empty():true, size():0, capacity():10
VectorPerson::~VectorPerson(): pVector deleted   // 아래는 MultiManager::persons[]의 배열 객체 소멸임
Person::~Person():p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
Person::~Person():p3 13 83.3 true :100 Dunsan-ro Seo-gu Daejeon:
Person::~Person():p2 12 52.2 false :1001, Jungang-daero, Yeonje-gu, Busan:
Person::~Person():p1 11 61.1 true :Jong-ro 1-gil, Jongno-gu, Seoul:
Person::~Person():p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:

===============================================================================
== 문제 5 실행 결과 2: PersonManager::clear() 테스트
=============================================================================== 

******************************* Main Menu *********************************
...
Menu item number? 1
...
====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 1
display(): count 5
[0] p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:
[1] p1 11 61.1 true :Jong-ro 1-gil, Jongno-gu, Seoul:
[2] p2 12 52.2 false :1001, Jungang-daero, Yeonje-gu, Busan:
[3] p3 13 83.3 true :100 Dunsan-ro Seo-gu Daejeon:
[4] p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
empty():false, size():5, capacity():10

====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 3
Person::~Person():p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:
Person::~Person():p1 11 61.1 true :Jong-ro 1-gil, Jongno-gu, Seoul:
Person::~Person():p2 12 52.2 false :1001, Jungang-daero, Yeonje-gu, Busan:
Person::~Person():p3 13 83.3 true :100 Dunsan-ro Seo-gu Daejeon:
Person::~Person():p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
display(): count 0
empty():true, size():0, capacity():10

====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 1
display(): count 0
empty():true, size():0, capacity():10


/******************************************************************************
 * 문제 6
 ******************************************************************************/
// 아래 class Factory를 class VectorPerson와 class PersonManager 사이에 삽입하라.
//----------------------------------------------------------------------------

/******************************************************************************
 * ch4_2: Factory class
 ******************************************************************************/

class Factory
{
    Person* checkInputFormatError(istream* in, Person* p) {
        if (UI::checkDataFormatError(in)) { // 정수입력할 곳에 일반 문자 입력한 경우
            delete p;         // inputPerson(istream* in)에서 할당한 메모리 반납
            return nullptr;   // nullptr은 에러가 발생했다는 의미임
        }
        if (UI::echo_input) p->println(); // 자동체크에서 사용됨
        return p;
    }

public:
    // 동적으로 Person 객체를 할당 받은 후 키보드로부터 새로 추가하고자 하는 사람의 인적정보를 읽어 들여
    // 해당 객체에 저장한 후 그 객체의 포인터를 반환한다.
    Person* inputPerson(istream* in) {
        Person* p = new Person();
        p->input(in);
        return checkInputFormatError(in, p);
    }
};

//----------------------------------------------------------------------------
// 기존의 PersonManager 클래스에 아래 멤버를 기존 persons 멤버 선언 뒤에 추가하라.
//----------------------------------------------------------------------------
    Factory factory;

//----------------------------------------------------------------------------
// 기존의 PersonManager::append() { } 를 아래 두 함수로 대체하라.
//----------------------------------------------------------------------------

void PersonManager::printNotice(const string preMessage, const string postMessage) {
    cout << preMessage;
    cout << " [person information] " << postMessage << endl;
}

// 아래 함수는 사용자로부터 새로 추가할 Person 객체의 수를 입력 받고 for문을 이용하여 
// 그 개수만큼의 Person 객체를 생성하고 인적정보를 입력받은 후 (factory.inputPerson(&cin)을 통해)
// 그 객체 포인터를 VectorPerson persons의 맨 끝 원소로 추가한다.
 
/* append() 실행 시 아래 항목들을 복사해서 순서적으로 입력하면 편하게 인적정보를 입력할 수 있음
3
HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
LeeMongRyong 1 65 true :Jong-ro 1-gil, Jongno-gu, Seoul:
LeeSoonShin 2 80 true :1001, Jungang-daero, Yeonje-gu, Busan:
*/
void PersonManager::append() { // Menu item 2
    int count = UI::getPositiveInt("The number of persons to append? ");
    // to_string(10) 함수: 정수 10을 문자열 "10"으로 변환
    // stoi("10") 함수: 문자열 "10"을 정수 10으로 변환
    printNotice("Input "+to_string(count), ":");
    for (int i = 0; i < count; ++i) {
        Person* p = factory.inputPerson(&cin); // 한 사람 정보 입력 받음
        if (p) persons.push_back(p); // if (p != nullptr) 와 동일; 
        // 만약 p가 nullptr이면 이는 입력 시 에러가 발생한 것임 
        // (즉, 정수를 입력해야 하는 곳에 일반 문자를 입력한 경우)
    }
    display();
}

===============================================================================
== 문제 6 실행 결과
=============================================================================== 
...
====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 2
The number of persons to append? 3     // 사용자가 입력
Input 3 [person information] :         // 연속적으로 3 명의 인적 정보를 입력해야 함
Person::Person(...): 0 0 false ::      // Person* p = new Person();에서 출력
HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21: // 사용자 입력
Person::Person(...): 0 0 false ::
LeeMongRyong 1 65 true :Jong-ro 1-gil, Jongno-gu, Seoul:
Person::Person(...): 0 0 false ::
LeeSoonShin 2 80 true :1001, Jungang-daero, Yeonje-gu, Busan:
display(): count 8
[0] p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:
[1] p1 11 61.1 true :Jong-ro 1-gil, Jongno-gu, Seoul:
[2] p2 12 52.2 false :1001, Jungang-daero, Yeonje-gu, Busan:
[3] p3 13 83.3 true :100 Dunsan-ro Seo-gu Daejeon:
[4] p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
[5] HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
[6] LeeMongRyong 1 65 true :Jong-ro 1-gil, Jongno-gu, Seoul:
[7] LeeSoonShin 2 80 true :1001, Jungang-daero, Yeonje-gu, Busan:
empty():false, size():8, capacity():10


/******************************************************************************
 * 문제 7
 ******************************************************************************/
// 기존의 VectorPerson의 경우 초기에 설정된 allocSize보다 더 많은 포인터를 삽입하고자 할 경우
// 할당된 pVector[] 배열이 작아서 불가능했다. 여기서 pVector[]를 좀더 크게 확대시켜 보자.
// 아래 extend_capacity() 함수를 구현하라. 
// 그리고 기존 push_back(Person* p) 함수에 새로 서술된 내용을 추가하라.
//----------------------------------------------------------------------------

// pVector[]의 배열 크기가 작으면 extend_capacity()를 호출하여 확장한다.
void VectorPerson::push_back(Person* p) {
    pVector[] 백터가 가득 찼으면 
        extend_capacity()를 호출한다.
    pVector[count++] = p;
}

// pVector[]의 배열 크기를 두배로 확장한다.
void VectorPerson::extend_capacity() {
    Person **saved_persons = pVector; // 기존의 pVector를 백업함
    allocSize 값을 두 배로 늘린 후 새로 pVector를 할당 받는다.
    for 문을 이용하여 count 개수만큼만 
        saved_persons[i]에 저장된 포인터를 새로 할당 받은 pVector[i]에 저장한다. 
    saved_persons [배열] 메모리를 반납한다. (배열임을 명심할 것)
    cout << "VectorPerson: capacity extended to " << allocSize << endl;
}

===============================================================================
== 문제 7 실행 결과
=============================================================================== 

******************************* Main Menu *********************************
* 0.Exit 1.PersonManager(ch3_2, 4)                                        *
* 2.Class:Object(ch3_1)                                                   *
***************************************************************************
Menu item number? 1
...
display(): count 5
[0] p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:
[1] p1 11 61.1 true :Jong-ro 1-gil, Jongno-gu, Seoul:
[2] p2 12 52.2 false :1001, Jungang-daero, Yeonje-gu, Busan:
[3] p3 13 83.3 true :100 Dunsan-ro Seo-gu Daejeon:
[4] p4 14 64.4 false :88 Gongpyeong-ro, Jung-gu, Daegu:
empty():false, size():5, capacity():10
PersonManager::run() starts

====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 2
The number of persons to append? 5 // 같은 데이타를 5번 연속 삽입
Input 5 [person information] :
Person::Person(...): 0 0 false ::
HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
Person::Person(...): 0 0 false ::
HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
Person::Person(...): 0 0 false ::
HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
Person::Person(...): 0 0 false ::
HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
Person::Person(...): 0 0 false ::
HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
display(): count 10
...
[5] HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
[6] HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
[7] HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
[8] HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
[9] HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
empty():false, size():10, capacity():10

====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 2
The number of persons to append? 2        // 같은 데이타를 2번 연속 삽입
Input 2 [person information] :
Person::Person(...): 0 0 false ::
HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
VectorPerson: capacity extended to 20 /* 11번째 추가시 메모리가 두배로 확장되었음 */
Person::Person(...): 0 0 false ::
HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
display(): count 12
...
[9] HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
[10] HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
[11] HongGilDong 0 71.5 false :Gwangju Nam-gu Bongseon-dong 21:
empty():false, size():12, capacity():20

// 다시 한번 2번 메뉴를 실행한 후 9개를 반복하여 입력하면 40개로 확정되는 것을 확인하라.

/******************************************************************************
 * 문제 8
 ******************************************************************************/
// 4번 메뉴 항목을 구현하기 위해선 먼저 아래 함수들을 namespace UI의 getInt() 함수 앞에 추가하라.
//----------------------------------------------------------------------------

// 입력장치에서 하나의 단어로 구성된 문자열을 입력 받음
string getNext(const string msg) {
    cout << msg; // 입력용 메시지를 출력
    cin >> line; // 하나의 단어를 읽어 들임
    if (echo_input) cout << line << endl; // 자동체크 시 출력됨
    getline(cin, emptyLine); // 입력받은 한 단어 외 그 행의 나머지 데이타(엔터포함)는 읽어서 버림
    return line;             // 이유는 여기서 [엔터]를 제거하지 않으면 
}                            // 다음의 getNextLine()에서 엔터만 읽어 들일 수 있기 때문에

// 입력장치에서 한 행을 입력 받음
string getNextLine(const string msg) {
    cout << msg; // 입력용 메시지를 출력
    getline(cin, line); // 한 행을 읽어 들임
    if (echo_input) cout << line << endl; // 자동체크 시 출력됨
    return line;
}

//----------------------------------------------------------------------------
// 또한 class Person에 아래 멤버 데이타와 멤버 함수를 추가한 후
// getPasswd(), setPasswd(const string passwd) 함수를 완성하라.
//----------------------------------------------------------------------------
// 1) class Person의 name 멤버 뒤에 아래 멤버를 추가하라.
    string passwd;          // 비번
//
// 2) 아래 멤버 함수를 getName() 뒤에 추가하라.
    string      getPasswd()  { TODO: 적절한 멤버 값을 반환하라. }
//
// 3) 아래 멤버 함수를 setName() 뒤에 추가하라.
    void setPasswd(const string passwd)   { TODO: 매개변수 passwd를 상응하는 멤버에 저장하라. }

//----------------------------------------------------------------------------
// 기존 login() 함수를 아래 두 함수로 교체하고, 이 함수가 호출하는 findByName()를 구현하라.
//----------------------------------------------------------------------------

// VectorPerson에 저장된 사람들 중 매개변수 name과 동일한 이름을 가진 사람을 찾는다. 
Person* PersonManager::findByName(const string name) {
    for 문을 이용하여 persons에 저장된 각각(i)의 사람 객체에 대해
        매개변수 name과 비교해서 동일한 이름을 가진 객체이면 해당 객체의 포인터(Person*)를 반환한다.
        persons의 size(), at(i), at(i)->getName() 등의 멤버함수 활용하라.
    // 찾지 못한 경우   
    cout << name + ": NOT found" << endl;
    return nullptr;
}

// 사용자로부터 로그인할 사람의 이름과 비번을 입력받고 동일한 이름을 가진 Person 객체를
// persons에서 찾고 비번이 일치하는지 체크한 후 CurrentUser(p).run() 실행한다.
// 기존(ch4-1)의 Main Menu에서 호출하던 CurrentUser를 메뉴항목에서 삭제한 후
// 대신 여기서 호출함(사용자가 선택한 인적정보 p를 인자로 넘겨 주면서)
void PersonManager::login() {
    string name = UI::getNext("user name: ");
    Person* p = findByName(name); // 해당 사람을 VectorPerson에서 찾는다.
    if (p == nullptr) return;     // 해당 사람 존재하지 않음
    string passwd = UI::getNextLine("password: ");
    if (passwd != p->getPasswd()) // 비번 불일치
        cout << "WRONG password!!" << endl;
    else
        CurrentUser(p).run();
}

===============================================================================
== 문제 8 실행 결과
=============================================================================== 
...
====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 4
user name: p10        // 존재하지 않는 사용자인 경우
p10: NOT found

...
Menu item number? 4
user name: p0
password: pxc         // 비번이 틀린 경우 (초기 비번 없음)
WRONG password!!

...
Menu item number? 4
user name: p0
password: [엔터]        // 초기 비번 없음, 데이터 입력 없이 그냥 엔터

+++++++++++++++++++++ Current User Menu ++++++++++++++++++++++++
+ 0.Logout 1.Display 2.Getter 3.Setter 4.Set 5.WhatAreYouDoing +
+ 6.IsSame 7.InputPerson                                       +
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Menu item number? 1
p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:

...
Menu item number? 0

====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 


/******************************************************************************
 * 문제 9
 ******************************************************************************/
// 기존 class CurrentUser에 비밀번호를 변경하는 changePasswd() 멤버함수를 추가 해 보자.
// 1) 기존 CurrentUser::run() 함수에서 메뉴 내용인 menuStr을 아래 내용으로 대체하라.
//----------------------------------------------------------------------------
    string menuStr =
        "+++++++++++++++++++++ Current User Menu ++++++++++++++++++++++++\n"
        "+ 0.Logout 1.Display 2.Getter 3.Setter 4.Set 5.WhatAreYouDoing +\n"
        "+ 6.IsSame 7.InputPerson 8.ChangePasswd(4_2)                   +\n"
        "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n";

//----------------------------------------------------------------------------
// 2) 8번 메뉴항목을 실행하는 아래 함수를 CurrentUser::run() 앞에 추가하고 구현하라. 
//    구현시 PersonManager::login()을 참조하라.
//----------------------------------------------------------------------------
void CurrentUser::changePasswd() {
    UI::getNext("New password: ")를 사용해 비번을 입력 받고,
    pUser가 포인트하는 객체의 비번을 변경하라.
    cout << "Password changed" << endl;
}

//----------------------------------------------------------------------------
// 3) class CurrentUser에 changePasswd() 멤버함수 선언을 run() 선언 앞에 추가하라.
// 4) CurrentUser::run() 내의 func_arr[]의 맨 뒤에 적절한 함수 포인터를 추가하라.
// 5) 코딩 길이를 줄이기 위해 PersonManager::run() 내의 func_arr[]의 PM:: 표현을 참조하여 
//    CurrentUser::run() 내에 using CU = CurrentUser; 문장을 추가하고, 
//    func_arr[]의 모든 원소를 CU를 사용하여 짧게 줄여서 표현하라.
//----------------------------------------------------------------------------

===============================================================================
== 문제 9 실행 결과
=============================================================================== 
...
====================== Person Management Menu ===================
...
Menu item number? 4
user name: p0
password: 

+++++++++++++++++++++ Current User Menu ++++++++++++++++++++++++
+ 0.Logout 1.Display 2.Getter 3.Setter 4.Set 5.WhatAreYouDoing +
+ 6.IsSame 7.InputPerson 8.changePasswd(4_2)                   +
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Menu item number? 8
New password: p0
Password changed

...
Menu item number? 0

====================== Person Management Menu ===================
= 0.Exit 1.Display 2.Append 3.Clear 4.Login(CurrentUser, ch4_2) =
=================================================================
Menu item number? 4
user name: p0
password: [엔터]        // 데이터 입력 없이 그냥 엔터
WRONG password!!

...
Menu item number? 4
user name: p0
password: p0          // 새로 변경된 비번

+++++++++++++++++++++ Current User Menu ++++++++++++++++++++++++
...
Menu item number? 1
p0 10 70 false :Gwangju Nam-gu Bongseon-dong 21:



/******************************************************************************
 * 자동 오류 체크 모드로 프로그램 실행
 ******************************************************************************/
// 1. clc.chosun.ac.kr의 [강의자료실]에서 CH4_2 과제 테스트 파일을 다운받은 후 
//    압축 파일을 풀고 test 폴더를 드래깅하여 이클립스의 [Project Explorer]의 
//    [CH4_2] 프로젝트 위에 드랍한다. (test 폴더와 그 밑에 테스트용 파일이 있어야 함)
// 2. 기존 프로젝트 CH2의 src 폴드에 있는 check_error.h를 CH4_2 프로젝트의 
//    src 폴더로 복사하라. (파일 선택 후 [Ctrl+C], src 폴더를 선택 후 [Ctrl+V])
// 3. 소스 파일 맨 앞쪽에 있는 AUTOMATIC_ERROR_CHECK 상수 값을 true로 설정하라.
// 4. main() 함수 내의 evaluate(true)가 true로 설정되어 있는지 확인하라.
// 5. 프로그램 테스트를 위한 입출력 파일이 test 폴더에 다운로드 되어 있는지 확인하라.
// 6. 프로그램이 정상적으로 구현되었다면 아래 [프로그램 실행 결과]와 같이 출력될 것이다.

===============================================================================
== 1. 정상적인 프로그램 실행 결과
==    아래 각 테스트 번호는 위 문제 번호와는 관련 없습니다.
=============================================================================== 
test 1 : O
test 2 : O
test 3 : O
test 4 : O
test 5 : O
test 6 : O
test 7 : O
Good bye!!

===============================================================================
== 2. 비정상적인 경우의 프로그램 실행방법은 CH2의 실습과제 설명의 마지막 부분을 참조하기 바란다.  
=============================================================================== 

/******************************************************************************
 * 프로그램 제출
 ******************************************************************************/
// 1. 중요: 소스 파일 맨 앞쪽에 있는 AUTOMATIC_ERROR_CHECK 상수 값을 false로 설정하라.
// 2. 프로그램을 oj.chosun.ac.kr에 제출하라. 
//-----------------------------------------------------------------------------