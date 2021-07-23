/**
 */
package monitoringmm;

import org.eclipse.emf.common.util.EList;

import org.eclipse.emf.ecore.EClass;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>MO Agent</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link monitoringmm.MOAgent#getEclass <em>Eclass</em>}</li>
 *   <li>{@link monitoringmm.MOAgent#getElements <em>Elements</em>}</li>
 * </ul>
 *
 * @see monitoringmm.MonitoringmmPackage#getMOAgent()
 * @model
 * @generated
 */
public interface MOAgent extends MonitorableElement {
	/**
	 * Returns the value of the '<em><b>Eclass</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Eclass</em>' reference.
	 * @see #setEclass(EClass)
	 * @see monitoringmm.MonitoringmmPackage#getMOAgent_Eclass()
	 * @model
	 * @generated
	 */
	EClass getEclass();

	/**
	 * Sets the value of the '{@link monitoringmm.MOAgent#getEclass <em>Eclass</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Eclass</em>' reference.
	 * @see #getEclass()
	 * @generated
	 */
	void setEclass(EClass value);

	/**
	 * Returns the value of the '<em><b>Elements</b></em>' containment reference list.
	 * The list contents are of type {@link monitoringmm.MOElement}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Elements</em>' containment reference list.
	 * @see monitoringmm.MonitoringmmPackage#getMOAgent_Elements()
	 * @model containment="true"
	 * @generated
	 */
	EList<MOElement> getElements();

} // MOAgent
