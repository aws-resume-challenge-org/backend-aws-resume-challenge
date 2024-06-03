describe('DynamoDb Update Test', () => {
  const APIEndpoint = "https://7vgsgyibz8.execute-api.us-west-2.amazonaws.com/getVisitorCount"
  it('This should check that the number on my website is the same as in my database and it is in fact a valid number!', () => {
    // get starting value
    cy.request('GET', 'https://7vgsgyibz8.execute-api.us-west-2.amazonaws.com/getVisitorCount').then((response) => {
      expect(response.status).to.eq(200);

      const numberAsString = response.body;
      const number = parseFloat(numberAsString)

      expect(number).to.be.a('number');
      expect(number).to.be.greaterThan(0)

      const nextCall = (number + 1).toString();

      cy.visit("https://rcarrollresume.com/")
      expect(cy.contains(nextCall))
    })


    
    
  })
  
})