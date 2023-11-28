from entities.citation import CitationFactory
from repositories.citation_repository import CitationRepository


class CitationService:
    """Vastaa viitteiden hallinoimisesta. Luokan avulla voi lisätä/poistaa/listata viitteitä."""

    def __init__(self, citation_repository: CitationRepository) -> None:
        self._citation_repository = citation_repository

    def add_citation(self, data) -> None:
        """Lisää viitteen"""
        citation = CitationFactory.create(data)
        return self._citation_repository.add_citation(citation)

    def list_citations(self) -> list:
        """Palauttaa listan kaikista viitteistä"""
        citations = self._citation_repository.get_all_citations()
        return [CitationFactory.create(citation) for citation in citations]

    def delete_citation(self) -> None:
        """Poistaa viitteen"""
        pass
