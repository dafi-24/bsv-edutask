describe('Logging into the system', () => {
  // define variables that we need on multiple occasions
  let uid // user id
  let name // name of the user (firstName + ' ' + lastName)
  let email // email of the user

  before(function () {
    // create a fabricated user from a fixture
    cy.fixture('R8UC1.json')
      .then((user) => {
        cy.request({
          method: 'POST',
          url: 'http://localhost:5000/users/create',
          form: true,
          body: user
        }).then((response) => {
          uid = response.body._id.$oid
          name = user.firstName + ' ' + user.lastName
          email = user.email
        })
      })
  })

  beforeEach(function () {
    // enter the main main page

    cy.visit('http://localhost:3000');
    cy.get('h1').should('contain.text', 'Login');
    cy.contains('div', 'Email Address').find('input[type=text]').type(email);
    cy.get('form').submit();
    cy.get('#title').type('Todo from song');
    cy.get('#url').type('https://www.youtube.com/watch?v=XqZsoesa55w&list=RDXqZsoesa55w&start_radio=1');
    cy.get('[type="submit"]').click()
    cy.get('.container-element img').eq(0).click()

  })


  it('adding todo item', () => {
    
    cy.get('.inline-form > [type="text"]').type('test description')
    cy.get('.inline-form > [type="submit"]').click()
    cy.get('.todo-list li').should('have.length', 2)
    cy.get('.todo-list li').eq(1).should('contain.text', 'test description')
  })

  it('adding todo item when empty field', () => {
    cy.get('.inline-form > [type="submit"]').should('be.disabled');
  })

  after(function () {
    // clean up by deleting the user from the database
    

    cy.request({
      method: 'DELETE',
      url: `http://localhost:5000/users/${uid}`
    }).then((response) => {
      cy.log(response.body)
    })
  })
})