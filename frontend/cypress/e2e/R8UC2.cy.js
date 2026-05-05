describe('Logging into the system', () => {
  // define variables that we need on multiple occasions
  let uid // user id
  let name // name of the user (firstName + ' ' + lastName)
  let email // email of the user
  
  before(function () {
    // create a fabricated user from a fixture
    cy.fixture('R8UC2.json')
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
    



  it('should show completed', () => {
    
    cy.get('.inline-form > [type="text"]').type('test description')
    cy.get('.inline-form > [type="submit"]').click()
    cy.get(':nth-child(2) > .checker').click();
    cy.get(':nth-child(2) > .checked')
    cy.get(':nth-child(2) > .checker.checked + .editable').should('have.css', 'text-decoration').and('include', 'line-through');
  })

  it('should not have line-through and should be active', () => {
    
    cy.get(':nth-child(1) > .checker').click();
    cy.get(':nth-child(1) > .checker').should('have.class', 'checked');
    cy.get(':nth-child(1) > .checker').click();
  
    cy.get('.todo-list > :nth-child(1) > .editable').should('not.have.css', 'text-decoration-line', 'line-through')
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