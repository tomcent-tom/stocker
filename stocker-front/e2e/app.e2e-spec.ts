import { StockerFrontPage } from './app.po';

describe('stocker-front App', function() {
  let page: StockerFrontPage;

  beforeEach(() => {
    page = new StockerFrontPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
